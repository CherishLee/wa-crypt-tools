"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16version_features.proto"\xd6\x0f\n\x10Version_Features\x12\x18\n\x10whatsapp_version\x18\x01 \x01(\t\x12\x1a\n\x12substringedUserJid\x18\x03 \x01(\t\x12\x10\n\x03idk\x18\x04 \x01(\x08H\x00\x88\x01\x01\x12\x15\n\x08call_log\x18\x05 \x01(\x08H\x01\x88\x01\x01\x12\x18\n\x0blabeled_jid\x18\x06 \x01(\x08H\x02\x88\x01\x01\x12\x18\n\x0bmessage_fts\x18\x07 \x01(\x08H\x03\x88\x01\x01\x12\x19\n\x0cblank_me_jid\x18\x08 \x01(\x08H\x04\x88\x01\x01\x12\x19\n\x0cmessage_link\x18\t \x01(\x08H\x05\x88\x01\x01\x12\x19\n\x0cmessage_main\x18\n \x01(\x08H\x06\x88\x01\x01\x12\x19\n\x0cmessage_text\x18\x0b \x01(\x08H\x07\x88\x01\x01\x12\x19\n\x0cmissed_calls\x18\x0c \x01(\x08H\x08\x88\x01\x01\x12\x19\n\x0creceipt_user\x18\r \x01(\x08H\t\x88\x01\x01\x12\x1a\n\rmessage_media\x18\x0e \x01(\x08H\n\x88\x01\x01\x12\x1a\n\rmessage_vcard\x18\x0f \x01(\x08H\x0b\x88\x01\x01\x12\x1b\n\x0emessage_future\x18\x10 \x01(\x08H\x0c\x88\x01\x01\x12\x1b\n\x0emessage_quoted\x18\x11 \x01(\x08H\r\x88\x01\x01\x12\x1b\n\x0emessage_system\x18\x12 \x01(\x08H\x0e\x88\x01\x01\x12\x1b\n\x0ereceipt_device\x18\x13 \x01(\x08H\x0f\x88\x01\x01\x12\x1c\n\x0fmessage_mention\x18\x14 \x01(\x08H\x10\x88\x01\x01\x12\x1c\n\x0fmessage_revoked\x18\x15 \x01(\x08H\x11\x88\x01\x01\x12\x1d\n\x10broadcast_me_jid\x18\x16 \x01(\x08H\x12\x88\x01\x01\x12\x1d\n\x10message_frequent\x18\x17 \x01(\x08H\x13\x88\x01\x01\x12\x1d\n\x10message_location\x18\x18 \x01(\x08H\x14\x88\x01\x01\x12\x1d\n\x10participant_user\x18\x19 \x01(\x08H\x15\x88\x01\x01\x12\x1e\n\x11message_thumbnail\x18\x1a \x01(\x08H\x16\x88\x01\x01\x12\x1f\n\x12message_send_count\x18\x1b \x01(\x08H\x17\x88\x01\x01\x12 \n\x13migration_jid_store\x18\x1c \x01(\x08H\x18\x88\x01\x01\x12 \n\x13payment_transaction\x18\x1d \x01(\x08H\x19\x88\x01\x01\x12!\n\x14migration_chat_store\x18\x1e \x01(\x08H\x1a\x88\x01\x01\x12!\n\x14quoted_order_message\x18\x1f \x01(\x08H\x1b\x88\x01\x01\x12"\n\x15media_migration_fixer\x18  \x01(\x08H\x1c\x88\x01\x01\x12$\n\x17quoted_order_message_v2\x18! \x01(\x08H\x1d\x88\x01\x01\x12&\n\x19message_main_verification\x18" \x01(\x08H\x1e\x88\x01\x01\x12-\n quoted_ui_elements_reply_message\x18# \x01(\x08H\x1f\x88\x01\x01\x12G\n:alter_message_ephemeral_to_message_ephemeral_remove_column\x18$ \x01(\x08H \x88\x01\x01\x12W\nJalter_message_ephemeral_setting_to_message_ephemeral_setting_remove_column\x18% \x01(\x08H!\x88\x01\x01B\x06\n\x04_idkB\x0b\n\t_call_logB\x0e\n\x0c_labeled_jidB\x0e\n\x0c_message_ftsB\x0f\n\r_blank_me_jidB\x0f\n\r_message_linkB\x0f\n\r_message_mainB\x0f\n\r_message_textB\x0f\n\r_missed_callsB\x0f\n\r_receipt_userB\x10\n\x0e_message_mediaB\x10\n\x0e_message_vcardB\x11\n\x0f_message_futureB\x11\n\x0f_message_quotedB\x11\n\x0f_message_systemB\x11\n\x0f_receipt_deviceB\x12\n\x10_message_mentionB\x12\n\x10_message_revokedB\x13\n\x11_broadcast_me_jidB\x13\n\x11_message_frequentB\x13\n\x11_message_locationB\x13\n\x11_participant_userB\x14\n\x12_message_thumbnailB\x15\n\x13_message_send_countB\x16\n\x14_migration_jid_storeB\x16\n\x14_payment_transactionB\x17\n\x15_migration_chat_storeB\x17\n\x15_quoted_order_messageB\x18\n\x16_media_migration_fixerB\x1a\n\x18_quoted_order_message_v2B\x1c\n\x1a_message_main_verificationB#\n!_quoted_ui_elements_reply_messageB=\n;_alter_message_ephemeral_to_message_ephemeral_remove_columnBM\nK_alter_message_ephemeral_setting_to_message_ephemeral_setting_remove_columnb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'version_features_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_VERSION_FEATURES']._serialized_start = 27
    _globals['_VERSION_FEATURES']._serialized_end = 2033