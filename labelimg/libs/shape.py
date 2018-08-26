#!/usr/bin/python
# -*- coding: utf-8 -*-
# from config import PEN_SIZE, TRANSLUCENT

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except ImportError:
    pass
    # from PyQt4.QtGui import *
    # from PyQt4.QtCore import *

from libs.lib import distance
from libs.config import CConfig

import sys

DEFAULT_LINE_COLOR = QColor(0, 255, 0, 128)
DEFAULT_FILL_COLOR = QColor(255, 0, 0, 128)
DEFAULT_SELECT_LINE_COLOR = QColor(255, 255, 255)
DEFAULT_SELECT_FILL_COLOR = QColor(0, 128, 255, 155)
DEFAULT_VERTEX_FILL_COLOR = QColor(0, 255, 0, 255)
DEFAULT_HVERTEX_FILL_COLOR = QColor(255, 0, 0)


class Shape(object):
    P_SQUARE, P_ROUND = range(2)

    MOVE_VERTEX, NEAR_VERTEX = range(2)

    # The following class variables influence the drawing
    # of _all_ shape objects.
    line_color = DEFAULT_LINE_COLOR
    fill_color = DEFAULT_FILL_COLOR
    select_line_color = DEFAULT_SELECT_LINE_COLOR
    select_fill_color = DEFAULT_SELECT_FILL_COLOR
    vertex_fill_color = DEFAULT_VERTEX_FILL_COLOR
    hvertex_fill_color = DEFAULT_HVERTEX_FILL_COLOR
    point_type = P_ROUND
    point_size = 8
    scale = 1.0

    def __init__(self, label=None, line_color=None, difficult=False, paintLabel=False):
        self.label = label
        self.points = []
        self.fill = False
        self.selected = False
        self.difficult = difficult
        self.paintLabel = paintLabel

        self._highlightIndex = None
        self._highlightMode = self.NEAR_VERTEX
        self._highlightSettings = {
            self.NEAR_VERTEX: (40, self.P_ROUND),
            self.MOVE_VERTEX: (10.5, self.P_SQUARE),
        }

        self._closed = False

        if line_color is not None:
            # Override the class line_color attribute
            # with an object attribute. Currently this
            # is used for drawing the pending line a different color.
            self.line_color = line_color

    def close(self):
        self._closed = True

    def reachMaxPoints(self):
        if len(self.points) >= 4:
            return True
        return False

    def addPoint(self, point):
        if not self.reachMaxPoints():
            self.points.append(point)

    def popPoint(self):
        if self.points:
            return self.points.pop()
        return None

    def isClosed(self):
        return self._closed

    def setOpen(self):
        self._closed = False

    def paint(self, painter):
        config = CConfig()
        if self.points:
            color = self.select_line_color if self.selected else self.line_color
            if not self.selected:
                color.setAlpha(config.SETTING_TRANSPARENCY)
            pen = QPen(color)
            # Try using integer sizes for smoother drawing(?)
            pen.setWidth(max(config.SETTING_PEN_SIZE, int(round(2.0 / self.scale))))
            painter.setPen(pen)

            line_path = QPainterPath()
            vrtx_path = QPainterPath()

            line_path.moveTo(self.points[0])
            # Uncommenting the following line will draw 2 paths
            # for the 1st vertex, and make it non-filled, which
            # may be desirable.
            # self.drawVertex(vrtx_path, 0)

            for i, p in enumerate(self.points):
                line_path.lineTo(p)
                self.drawVertex(vrtx_path, i)
            if self.isClosed():
                line_path.lineTo(self.points[0])

            painter.drawPath(line_path)
            painter.drawPath(vrtx_path)
            painter.fillPath(vrtx_path, self.vertex_fill_color)

            # Draw text
            self.fontSize = int(line_path.length() / 38)
            self.fontSize = max(self.fontSize, config.SETTING_FONT_SIZE)
            if self.paintLabel:
                positionFlag = True if (self.points[0].y() - self.fontSize * 1.05) > 0 else False
                positionBotFlag = True if (self.points[2].y() - self.fontSize * 1.05) > 0 else False
                reversedShapeFlag = True if (self.points[2].y() < self.points[0].y()) else False
                halfOfLabel = int((len(self.label) / 2) * (self.fontSize * 0.7))

                xPosition = ((self.points[1].x() + self.points[0].x()) / 2) - halfOfLabel
                if not reversedShapeFlag:
                    if positionFlag:
                        yPosition = self.points[0].y() - self.fontSize * 0.5
                    elif not positionFlag:
                        yPosition = self.points[2].y() + self.fontSize * 1.34
                else:
                    if positionBotFlag:
                        yPosition = self.points[2].y() - self.fontSize * 0.5
                    elif not positionBotFlag:
                        yPosition = self.points[0].y() + self.fontSize * 1.34

                font = QFont()
                font.setPointSize(self.fontSize)
                font.setBold(False)
                painter.setFont(font)
                if (self.label == None):
                    self.label = ""

                color.setAlpha(config.SETTING_TEXT_TRANSPARENCY)
                pen = QPen(color)
                painter.setPen(pen)
                painter.drawText(xPosition, yPosition, self.label)

            if self.fill:
                color = self.select_fill_color if self.selected else self.fill_color
                if not self.selected:
                    color.setAlpha(config.SETTING_TRANSPARENCY)
                painter.fillPath(line_path, color)

    def drawVertex(self, path, i):
        d = self.point_size / self.scale
        shape = self.point_type
        point = self.points[i]
        if i == self._highlightIndex:
            size, shape = self._highlightSettings[self._highlightMode]
            d *= size
        if self._highlightIndex is not None:
            self.vertex_fill_color = self.hvertex_fill_color
        else:
            self.vertex_fill_color = Shape.vertex_fill_color
        if shape == self.P_SQUARE:
            path.addRect(point.x() - d / 2, point.y() - d / 2, d, d)
        elif shape == self.P_ROUND:
            path.addEllipse(point, d / 2.0, d / 2.0)
        else:
            assert False, "unsupported vertex shape"

    def nearestVertex(self, point, epsilon):
        for i, p in enumerate(self.points):
            if distance(p - point) <= epsilon:
                return i
        return None

    def containsPoint(self, point):
        return self.makePath().contains(point)

    def makePath(self):
        path = QPainterPath(self.points[0])
        for p in self.points[1:]:
            path.lineTo(p)
        return path

    def boundingRect(self):
        return self.makePath().boundingRect()

    def moveBy(self, offset):
        self.points = [p + offset for p in self.points]

    def moveVertexBy(self, i, offset):
        self.points[i] = self.points[i] + offset

    def highlightVertex(self, i, action):
        self._highlightIndex = i
        self._highlightMode = action

    def highlightClear(self):
        self._highlightIndex = None

    def copy(self):
        shape = Shape("%s" % self.label)
        shape.points = [p for p in self.points]
        shape.fill = self.fill
        shape.selected = self.selected
        shape._closed = self._closed
        if self.line_color != Shape.line_color:
            shape.line_color = self.line_color
        if self.fill_color != Shape.fill_color:
            shape.fill_color = self.fill_color
        shape.difficult = self.difficult
        return shape

    def __len__(self):
        return len(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value
