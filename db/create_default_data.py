from db.write import WriteQuote, WriteInfoFooter, WriteLinkSocial, ConditionVideoDB, OrderPhotoShootDB, \
    PreviewTextContactPageDB


def first_data_creation() -> None:
    # Создание столбцов с дефолтными значениями
    WriteQuote.default_quote()
    WriteInfoFooter.default_info_and_link_footer()
    WriteLinkSocial.default_link_social()
    ConditionVideoDB.create_default_condition_video()
    OrderPhotoShootDB.create_default_condition_video()
    PreviewTextContactPageDB.create_default_text()