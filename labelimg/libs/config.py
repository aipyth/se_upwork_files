class CConfig(object):
    _instance = None
    def __new__(cls_, *args, **kwargs):
        if not isinstance(cls_._instance, cls_):
            cls_.SETTING_PEN_SIZE = 10
            cls_.SETTING_TRANSPARENCY = 128
            cls_.SETTING_FONT_SIZE = 20
            cls_.SETTING_LABEL_INDENT = 30
            cls_._instance = object.__new__(cls_, *args, **kwargs)
        return cls_._instance