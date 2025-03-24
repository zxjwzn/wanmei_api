from enum import IntEnum

class LaaderProtocol:
    class MessageType(IntEnum):
        MT_BEGIN_NUMBER = 9001
        MT_CREATE_TEAM_REQ = 9002
        MT_CREATE_TEAM_RES = 9003
        MT_ENTER_TEAM_REQ = 9004
        MT_ENTER_TEAM_RES = 9005
        MT_ENTER_TEAM_NOTIFY = 9006
        MT_LEAVE_TEAM_REQ = 9007
        MT_LEAVE_TEAM_RES = 9008
        MT_LEAVE_TEAM_NOTIFY = 9009
        MT_KICK_TEAM_PLAYER_REQ = 9010
        MT_KICK_TEAM_PLAYER_RES = 9011
        MT_KICK_TEAM_PLAYER_NOTIFY = 9012
        MT_TEAM_CHAT_REQ = 9013
        MT_TEAM_CHAT_RES = 9014
        MT_TEAM_CHAT_NOTIFY = 9015
        MT_UPDATE_TEAM_INFO_REQ = 9016
        MT_UPDATE_TEAM_INFO_RES = 9017
        MT_UPDATE_TEAM_INFO_NOTIFY = 9018
        MT_MATCH_REQ = 9019
        MT_MATCH_RES = 9020
        MT_MATCH_NOTIFY = 9021
        MT_CANCEL_MATCH_REQ = 9022
        MT_CANCEL_MATCH_RES = 9023
        MT_CANCEL_MATCH_NOTIFY = 9024
        MT_GAME_INFO_NOTIFY = 9025
        MT_CREATE_GAME_NOTIFY = 9026
        MT_GAME_READY_REQ = 9027
        MT_GAME_READY_RES = 9028
        MT_GAME_READY_NOTIFY = 9029
        MT_GAME_START_NOTIFY = 9030
        MT_REMATCH_NOTIFY = 9031
        MT_GAME_OVER_NOTIFY = 9032
        MT_ZONES_INFO_NOTIFY = 9033
        MT_PING_ZONES_REPORT = 9034
        MT_CLIENT_GIVEUP_GAME_REQ = 9035
        MT_CLIENT_GIVEUP_GAME_RES = 9036
        MT_PLAYER_ESCAPE_NOTIFY = 9037
        MT_INVITE_FRIEND_REQ = 9038
        MT_INVITE_FRIEND_RES = 9039
        MT_MATCH_INVITED_NOTIFY = 9040
        MT_HANDLE_MATCH_INVITED_REQ = 9041
        MT_HANDLE_MATCH_INVITED_RES = 9042
        MT_HANDLE_MATCH_INVITED_NOTIFY = 9043
        MT_CLIENT_QUERY_TEAM_INFO_REQ = 9044
        MT_CLIENT_QUERY_TEAM_INFO_RES = 9045
        MT_TEAM_UPDATE_SLOT_REQ = 9046
        MT_TEAM_UPDATE_SLOT_RES = 9047
        MT_TEAM_UPDATE_SLOT_REQ_NOTIFY = 9048
        MT_TEAM_HANDLE_UPDATE_SLOT_REQ = 9049
        MT_TEAM_HANDLE_UPDATE_SLOT_RES = 9050
        MT_TEAM_HANDLE_UPDATE_SLOT_NOTIFY = 9051
        MT_TEAM_SLOT_CHANGED_NOTIFY = 9052
        MT_TEAM_UPDATE_ALLSLOT_REQ = 9053
        MT_TEAM_UPDATE_ALLSLOT_RES = 9054
        MT_TEAM_SET_SINGLE_MODE_REQ = 9055
        MT_TEAM_SET_SINGLE_MODE_RES = 9056
        MT_ROLL_SCENE_NOTF = 9057
        MT_SERVER_PINGS_NOTF = 9058
        MT_BAN_MAP_REQ = 9059
        MT_BAN_MAP_RES = 9060
        MT_BAN_ZONE_REQ = 9061
        MT_BAN_ZONE_RES = 9062
        MT_REJECT_COMBINE_TEAM_REQ = 9063
        MT_REJECT_COMBINE_TEAM_RES = 9064
        MT_INVITE_COMBINE_TEAM_REQ = 9065
        MT_INVITE_COMBINE_TEAM_RES = 9066
        MT_INVITE_COMBINE_TEAM_NOTIFY = 9067
        MT_HANDLE_INVITE_COMBINE_TEAM_REQ = 9068
        MT_HANDLE_INVITE_COMBINE_TEAM_RES = 9069
        MT_HANDLE_INVITE_COMBINE_TEAM_NOTIFY = 9070
        MT_COMBINE_TEAM_NOTIFY = 9071
        MT_APPLY_COMBINE_TEAM_REQ = 9072
        MT_APPLY_COMBINE_TEAM_RES = 9073
        MT_APPLY_COMBINE_TEAM_NOTIFY = 9074
        MT_HANDLE_APPLY_COMBINE_TEAM_REQ = 9075
        MT_HANDLE_APPLY_COMBINE_TEAM_RES = 9076
        MT_HANDLE_APPLY_COMBINE_TEAM_NOTIFY = 9077
        MT_CSGO_LAUNCH_SUC_REPORT = 9078
        MT_ABNORMAL_PLAYER_STATUS_NOTIFY = 9079
        MT_MODE_SWITCH_REQ = 9080
        MT_MODE_SWITCH_RES = 9081
        MT_OB_SETTING_REQ = 9082
        MT_OB_SETTING_RES = 9083
        MT_TRANSFER_CAPTAIN_REQ = 9084
        MT_TRANSFER_CAPTAIN_RES = 9085
        MT_APPLY_TRANSFER_CAPTAIN_NOTF = 9086
        MT_HANDLE_TRANSFER_CAPTAIN_REQ = 9087
        MT_HANDLE_TRANSFER_CAPTAIN_RES = 9088
        MT_HANDLE_TRANSFER_CAPTAIN_NOTF = 9089
        MT_TRANSFER_CAPTAIN_NOTF = 9090
        MT_BP_ORDER_REQ = 9091
        MT_BP_ORDER_RES = 9092
        MT_PICK_PLAYER_REQ = 9093
        MT_PICK_PLAYER_RES = 9094
        MT_PICK_CAMP_REQ = 9095
        MT_PICK_CAMP_RES = 9096
        MT_TEAM_SET_ABSGREEN_MODE_REQ = 9097
        MT_TEAM_SET_ABSGREEN_MODE_RES = 9098
        MT_TEAM_SET_ABSGREEN_MODE_NOTIFY = 9099
        MT_STRENGTH_DISPLAY_NOTF = 9100
        MT_CREATE_RECRUIT_MSG_REQ = 9101
        MT_CREATE_RECRUIT_MSG_RES = 9102
        MT_UPDATE_RECRUIT_MSG_NOTF = 9103
        MT_HIDE_RECRUIT_MSG_REQ = 9104
        MT_HIDE_RECRUIT_MSG_RES = 9105
        MT_GET_RECRUIT_LIST_REQ = 9106
        MT_GET_RECRUIT_LIST_RES = 9107
        MT_ENTER_RECRUIT_ROOM_REQ = 9108
        MT_ENTER_RECRUIT_ROOM_RES = 9109
        MT_QUICK_ENTER_RECRUIT_ROOM_REQ = 9110
        MT_QUICK_ENTER_RECRUIT_ROOM_RES = 9111
        MT_UPDATE_RECRUIT_MSG_REQ = 9112
        MT_UPDATE_RECRUIT_MSG_RES = 9113
        MT_1V1_BATTLE_REQ = 9114
        MT_1V1_BATTLE_RES = 9115
        MT_1V1_BATTLE_NOTF = 9116
        MT_HANDLE_1V1_BATTLE_REQ = 9117
        MT_HANDLE_1V1_BATTLE_RES = 9118
        MT_HANDLE_1V1_BATTLE_NOTF = 9119
        MT_CUSTOM_READY_REQ = 9120
        MT_CUSTOM_READY_RES = 9121
        MT_CUSTOM_READY_NOTF = 9122
        MT_TEAM_SET_ABSBALANCE_MODE_REQ = 9123
        MT_TEAM_SET_ABSBALANCE_MODE_RES = 9124
        MT_TEAM_SET_ABSBALANCE_MODE_NOTIFY = 9125
        MT_RECRUIT_MSG_PUSH_NOTF = 9126
        MT_DEL_RECRUIT_MSG_REQ = 9127
        MT_DEL_RECRUIT_MSG_RES = 9128
        MT_DEL_RECRUIT_MSG_NOTF = 9129
        MT_IN_PAGE_REPORT_REQ = 9130
        MT_IN_PAGE_REPORT_RES = 9131
        MT_LEAVE_PAGE_REQ = 9132
        MT_LEAVE_PAGE_RES = 9133
        MT_GET_IN_PAGE_COUNTS_REQ = 9134
        MT_GET_IN_PAGE_COUNTS_RES = 9135
        MT_GET_SORT_RECRUIT_LIST_REQ = 9136
        MT_GET_SORT_RECRUIT_LIST_RES = 9137
        MT_GET_MY_RECRUIT_LIST_REQ = 9138
        MT_GET_MY_RECRUIT_LIST_RES = 9139
        MT_PASSWORD_ENTER_RECRUIT_REQ = 9140
        MT_PASSWORD_ENTER_RECRUIT_RES = 9141
        MT_APPLY_ENTER_RECRUIT_REQ = 9142
        MT_APPLY_ENTER_RECRUIT_RES = 9143
        MT_APPLY_ENTER_RECRUIT_NOTF = 9144
        MT_HANDLE_APPLY_ENTER_RECRUIT_REQ = 9145
        MT_HANDLE_APPLY_ENTER_RECRUIT_RES = 9146
        MT_HANDLE_APPLY_ENTER_RECRUIT_NOTF = 9147
        MT_RECRUIT_MSG_BROADCAST = 9148
        MT_SET_SLOT_INFO_REQ = 9149
        MT_SET_SLOT_INFO_RES = 9150
        MT_SET_SLOT_INFO_NOTF = 9151
        MT_RELEASE_GAME_REQ = 9152
        MT_RELEASE_GAME_RES = 9153
        MT_SEARCH_RECRUIT_REQ = 9154
        MT_SEARCH_RECRUIT_RES = 9155
        MT_CREATE_CHANNNEL = 9156
        MT_DISMISS_CHANNNEL = 9157
        MT_UPDATE_GAME_VERSION_REQ = 9158
        MT_UPDATE_GAME_VERSION_RES = 9159
        MT_UPDATE_GAME_VERSION_NOTF = 9160
        MT_CHALLENGE_REQ = 9161
        MT_CHALLENGE_RES = 9162
        MT_CHALLENGE_NOTF = 9163
        MT_HANDLE_CHALLENGE_REQ = 9164
        MT_HANDLE_CHALLENGE_RES = 9165
        MT_HANDLE_CHALLENGE_NOTF = 9166
        MT_CANCEL_READY_REQ = 9167
        MT_CANCEL_READY_RES = 9168
        MT_CANCEL_READY_NOTF = 9169
        MT_CS2_CLIENT_VERSION_REPORT = 9170
        MT_ROLL_REQ = 9171
        MT_ROLL_RES = 9172
        MT_CANCEL_BAN_MAP_REQ = 9173
        MT_CANCEL_BAN_MAP_RES = 9174
        MT_CANCEL_PICK_CAMP_REQ = 9175
        MT_CANCEL_PICK_CAMP_RES = 9176
        MT_END_NUMBER = 9500

    class CSGOMatchMode(IntEnum):
        MATCH_MODE_NONE = 0
        MATCH_MODE_RANK_MATCH = 1
        MATCH_MODE_COUSTOM = 2
        MATCH_MODE_TOURNAMENT = 3
        MATCH_MODE_ENJOY = 4
        MATCH_MODE_RANK_BALANCE_MATCH = 5
        MATCH_MODE_RANK_PURE_MATCH = 6
        MATCH_MODE_RANK_GRUDGE_MATCH = 7
        MATCH_MODE_RANK_SINGLE = 8

    class ErrorCode(IntEnum):
        ERROR_OK = 0
        ERROR_NO_ENOUGH_ROOM = 1
        ERROR_INVALID_REQUEST_ARGUMENT = 2
        ERROR_NOT_TEAM_LEADER = 3
        ERROR_INVALD_REQEST = 4
        ERROR_PLAYER_EXISIT = 5
        ERROR_TEAM_NOT_FOUND = 6
        ERROR_MATCH_NOT_FOUND = 7
        ERROR_GAME_NOT_FOUND = 8
        ERROR_SERVER_IS_BUSY = 9
        ERROR_PLAYER_NOT_FOUND = 10
        ERROR_TEAM_FULL = 11
        ERROR_TEAM_NOT_FULL = 12
        ERROR_PLAYER_BANED = 13
        ERROR_SCORE_RANGE_LIMIT = 14
        ERROR_UNKOWN = 15
        ERROR_TEAM_IS_PLAYING = 16
        ERROR_IN_MATCHING = 17
        ERROR_IN_PLAYING = 18
        ERROR_SERVER_IS_MANTAINS = 19
        ERROR_NOT_IN_WHITE_LIST = 20
        ERROR_NOT_IN_CUPID_LIST = 21
        ERROR_NOT_IN_OPEN_TIME = 22
        ERROR_LEVEL_IS_LIMITED = 23
        ERROR_SERVER_INTERNAL_ERROR = 24
        ERROR_GET_TICKET_INFO_FAIL = 25
        ERROR_GET_TICKET_INFO_TIMEOUT = 26
        ERROR_NO_TICKET = 27
        ERROR_NOT_TEAM_MEMBER = 28
        ERROR_NOT_ONE_MEMBER = 29
        ERROR_NOT_SUPPORT = 30
        ERROR_CSGO_BANED = 31
        ERROR_IS_CREATING = 32
        ERROR_IDENTITY_MISMATCH = 33
        ERROR_NO_PERMISSION = 34
        ERROR_INVALID_ZONES = 35
        ERROR_TEAM_REJECT_COMBINE = 36
        ERROR_NO_MORE_DATA = 37
        ERROR_NO_RECRUIT_COUNT = 38
        ERROR_RECRUIT_CREATED = 39
        ERROR_RECRUIT_CANCELED = 40
        ERROR_NO_MATCH_RECRUIT_MSG = 41
        ERROR_IS_NERER = 42
        ERROR_INVALID_GRADE = 43
        ERROR_PLAYER_FORBIDEN = 44
        ERROR_NOT_GREEN = 45
        ERROR_KICKED_TOO_MUCH = 46
        ERROR_INVALID_WIN_RATE = 47
        ERROR_INVALID_RATING_PRO = 48
        ERROR_IS_SELF_ROOM = 49
        ERROR_MSG_SHIELD_SET = 50
        ERROR_PLAYER_MINORS = 51
        ERROR_PLAYER_NOT_REALNAME = 52
        ERROR_NOT_PWA = 53
        ERROR_USE_BANED_MAP = 54
        ERROR_INVALID_ROUNDS_NUMBER = 55
        ERROR_PLAYER_NOT_ALL_READY = 56
        ERROR_INVALID_RANK_COUNT = 57
        ERROR_INVALID_RANK_SCORE_GAP = 58
        ERROR_INVALID_RANK_RATINGPRO_GAP = 59
        ERROR_INVALID_RANK_PLAYER_COUNT = 60
        ERROR_PRE_RANK = 61
        ERROR_PASSWORD = 62
        ERROR_HAS_APPLYED = 63
        ERROR_TOO_MUCH_APPLYERS = 64
        ERROR_HAS_EXPIRED = 65
        ERROR_IN_OTHER_TEAM = 66
        ERROR_PLAYER_OFFLINE = 67
        ERROR_INVALID_LADDER_SCORE_GAP = 68
        ERROR_ANCHOR_TICKET_COUNT = 69
        ERROR_NOT_ENOUGH_ANCHOR_TICKET = 70
        ERROR_NOT_IN_ANCHOR_WHITELIST = 71
        ERROR_INVITING_LIMITED = 72
        ERROR_INVITE_COUNT_LIMITED = 73
        ERROR_NO_GAME_VERSION = 74
        ERROR_NOT_MATCH_GAME_VERSION = 75
        ERROR_INVALID_LADDER_SCORE_GAP_FOR_A = 76
        ERROR_INVALID_LADDER_SCORE_GAP_FOR_B = 77
        ERROR_GRUDGE_OPPONENT_NOT_READY = 78
        ERROR_HAS_GRUDGE_CHALLENGE = 79
        ERROR_NO_GRUDGE_LEFT_COUNT = 80
        ERROR_FORBID_FOUR_MATCHING = 81
        ERROR_CS2_UPDATING = 82
        ERROR_CS2_CLIEN_NEED_UPDATE = 83
        ERROR_HAS_NEWER = 84
        ERROR_TOO_MANY_PLAYERS = 85
        ERROR_HAS_DANGER_PLAYER = 86
        MAX_ERROR_SIZE = 87

    class BpAction(IntEnum):
        NEED_SERVER_BAN = 0
        NEED_SERVER_PICK = 1
        NEED_PLAYER_BAN = 2
        NEED_PLAYER_PICK = 3
        PLAYER_BAN = 4
        PLAYER_PICK = 5
        SERVER_BAN = 6
        SERVER_PICK = 7

    class RollSceneState(IntEnum):
        NONE = 0
        BAN_MAP = 1
        DISPLAY_BAN_MAP = 2
        BAN_ZONE = 3
        DISPLAY_BAN_ZONE = 4
        READY = 5
        DISPLAY_ROLL = 6
        SELECT_BP_ORDER = 7
        PICK_PLAYER = 8
        DISPLAY_PICK_PLAYER = 9
        PICK_CAMP = 10
        DISPLAY_PICK_CAMP = 11
        FINISHED = 12
        ROLL = 13

    class BpState(IntEnum):
        NONE = 0
        BANED = 1
        PICKED = 2

    class BpOrderAction(IntEnum):
        NONE = 0
        GIVEUP = 1
        PICK_PLAYER = 2
        BAN_MAP = 3
        COUNT = 4

    class BpOrderResult(IntEnum):
        NONE = 0
        PICK_PLAYER = 1
        BAN_MAP = 2

    class RollAction(IntEnum):
        NEED_ROLL = 0
        TIMEOUT_GIVEUP = 1
        ROLL = 2
        COUT = 3

    class GameStatus(IntEnum):
        ENTER_GAME = 0
        READY = 1
        CREATE_HOST = 2
        GAME_START = 3
        ROOM_CLOSE = 4
        ROLL = 5
        STRENGTH_DISPLAY = 6
        GAME_ABNORMAL = 7

    class GameVersion(IntEnum):
        NONE_VERSION = 0
        VERSION_A = 1
        VERSION_B = 2

    class PlayerFlags(IntEnum):
        FLAG_READY = 1
        FLAG_LEAVE = 2
        FLAG_ESCAPE = 4
        FLAG_LEAVE_TAG = 8
        FLAG_BANED = 16
        FLAG_KICK = 32
        FLAG_GIVEUP = 64

    class PlayerStatus(IntEnum):
        NONE = 0
        IS_READY = 1

    class MatchState(IntEnum):
        MATCH_STATE_NONE = 0
        MATCH_STATE_MATCHING = 1
        MATCH_STATE_IN_ROOM = 2
        MATCH_STATE_IN_GAME = 3
        MAX_MATCH_STATE_SIZE = 4

    class CustomTeamMode(IntEnum):
        CUSTOM_MODE = 0
        CAPTAIN_MODE = 1
        PWA_1V1_MODE = 2
        ONE_MANY_ARMY = 3

    class RedPacketsType(IntEnum):
        NO_RED_PACKETS = 0
        RED_PACKETS_MODE1 = 1

    class ChildRecruitType(IntEnum):
        DEFAULT = 0
        ANCHOR_RECRUIT_TYPE = 1
        SCORE_RECRUIT_TYPE = 2

    class CancelReason(IntEnum):
        CANCLE_NONE = 0
        CANCEL_ERROR_NOT_READY = 1
        CANCEL_ERROR_ADD_INTO_POOL = 2
        CANCEL_PLAYER_CANCEL = 3
        CANCEL_PLAYER_EXIT = 4
        CACNEL_CREATE_HOST_FAILED = 5
        CANCEL_SERVER_MAINTAINS = 6
        CANCEL_TEAM_LEADER_EXIT = 7
        CANCEL_ERROR_UNKOWN = 8

    class EnterChannel(IntEnum):
        DEFAULT = 0
        RECRUIT_CHANNEL = 1

    class LeaveTeamReason(IntEnum):
        NONE = 0
        ENTER_ANOTHER_MATCH = 1

    class ChatType(IntEnum):
        CUSTOM = 0
        SYSTEM = 1

    class RematchReason(IntEnum):
        NONE = 0
        OPPOSITE_NOT_READY = 1
        GAME_ROOM_FULL = 2

    class GameOverReason(IntEnum):
        GAME_OVER_NORMAL = 0
        GAME_OVER_ALL_PLAYER_LEAVE = 1
        GAME_OVER_CANCEL = 2
        GAME_OVER_SERVICE_ERROR = 3
        GAME_OVER_PLAYER_BAN = 4
        GAME_OVER_PLAYER_PAC = 5
        GAME_OVER_SURRENDER = 6

    class HandleInviteAction(IntEnum):
        Ignore = 0
        Accept = 1

    class Team_State(IntEnum):
        NONE = 0
        BUILDING = 1
        IN_POOL = 2

    class UpdateSlotReqType(IntEnum):
        UpdateType_ByPlayerId = 0
        UpdateType_BySlotPos = 1

    class HandleAction(IntEnum):
        AGREE = 0
        REJECT = 1

    class HandleApplyAction(IntEnum):
        Ignore = 0
        Accept = 1

    class MatchingGrading(IntEnum):
        DEFAULT = 0
        GRADING_D = 1
        GRADING_D_PLUS = 2
        GRADING_C = 3
        GRADING_C_PLUS = 4
        GRADING_B = 5
        GRADING_B_PLUS = 6
        GRADING_A = 7
        GRADING_A_PLUS = 8
        GRADING_S = 9

    class RecruitMsgStatus(IntEnum):
        UNPUBLISHED = 0
        PUBLISHED = 1
        EXPIRED = 2
        CANCELED = 4

    class RecruitType(IntEnum):
        RANK_RECRUIT_TYPE = 0
        CUSTOM_RECRUIT_TYPE = 1
        SOLO_RECRUIT_TYPE = 2
        ALL = 100

    class JoinRecruitType(IntEnum):
        ALL_IN_TYPE = 0
        PASSWORD_IN_TYPE = 1
        APPLY_IN_TYPE = 2

    class HandleBattleAction(IntEnum):
        Ignore = 0
        Accept = 1

    class PageType(IntEnum):
        SOCIAL_HALL = 1
        RECRUIT_HALL = 2
        MATCH_CENTER = 3
        APPOINT = 4

    class AwardType(IntEnum):
        ALL = 0
        NO_AWARD = 1
        HAS_AWARD = 2
    
    class GameType(IntEnum):
        DOTA = 1
        WAR3_1V1 = 2
        WAR3_2V2 = 3
        DOTA2 = 4
        IMBA = 5
        THIRD_SWORD = 6
        LZXF = 7
        CSGO = 8
        FILTER = 9
        AUTO_CHESS = 10

class GATETCPProtocol:
    class MessageType(IntEnum):
        MT_BEGIN_NUMBER = 10
        MT_HELLO_REQ = 10
        MT_HELLO_RES = 11
        MT_HELLO_NOTIFY = 12
        MT_KEEPALIVE_REQ = 13
        MT_KEEPALIVE_RES = 14
        MT_KEEPALIVE_NOTIFY = 15
        MT_END_NUMBER = 1000

    class ErrorCode(IntEnum):
        OK = 0
        SERVICE_MAINTAINING = -98
        SERVICE_NOT_RUN = -99
        TICKET_INVALID = -100
        LOGNAME_EXIST = -101
        LOGNAME_NOT_EXIST = -102
        PASSWORD_ERROR = -103
        USERID_INVALID = -104
        PASS_EXPIRYDATE = -105
        EMAIL_VERIFYCODE_ERROR = -106
        ACCOUNT_LOCKED = -107
        INVALID_ACCOUNT = -108
        CLIENT_VERSION_INVALID = -109
        ACCOUNT_ACCTIVED = -110
        VERIFYCODE_VERIFIED = -111
        USER_IN_BLACKLIST = -112
        LOGIN_CONNECT_ERROR = -113
        NICKNAME_DUPLICATE = -114
        GATE_SERVER_NORUN = -115
        LOGIN_SESSION_INVALID = -116
        USER_NOT_ONLINE = -117
        GAME_COUNT_MAX = -118
        GAME_PLAYER_COUNT_MAX = -119
        GAME_NOT_EXIST = -120
        GAME_LOCKED = -121
        GAME_OCCUPIED_SLOT = -122
        GAME_INVALID_SLOT = -123
        GAME_EXIST_USER = -124
        GAME_NOT_EXIST_USER = -125
        GAME_NOT_SLOT = -126
        GAME_NOT_MATCH_PLAYER_FULL = -127
        GAME_MATCH_TEAM_ID_INVALID = -128
        GAME_MATCH_CUP_ID__INVALID = -129
        GAME_MATCH_CUP_SCHEDULE_ID_INVALID = -130
        GAME_MATCH_HOST_NOT_RUN = -131
        GAME_MATCH_HOST_BUSY = -132
        GAME_MODE_INVALID = -133
        GAME_INVALID_GAME_ID = -150
        GAME_INVALID_ROLL_ACTION = -151
        GAME_INVALID_ROLL_SELECT_ACTION = -152
        GAME_ALREADY_EXIST = -153
        KICK_OUT = -200
        TIME_OUT = -201
        OTHER_LOGIN = -202
        INVALID_NICK_NAME = -203
        INVALID_INPUT_TEXT = -204
        GATE_DISCONNECT = -205
        INVALID_SIGN_NAME = -206
        PERMISSION_DENIED = -207
        ON_TEAM = -250
        TEAM_NAME_EXIST = -251
        TEAM_JOIN_REQUEST_EXIST = -252
        TEAM_LEADER_NOT_LEAVE = -253
        TEAM_NOT_MEMBER = -254
        SERVICE_RESTART = -300
        QUICK_LOGIN_FORBIDDEN = -301
        REQUEST_ERROR = -400
        REQUEST_TIMEOUT = -401
        DB_CONNECT_ERROR = -402
        DB_OPERATION_EXCEPTION = -403
        SYSTEM_BUSY = -404
        UNKOWN_ERROR = -405
        INVALID_REQUEST_ARGUMENT = -406
        INVALID_STEAM_ID = 407
        CAPTAIN_ALREADY_CHOOSE = -408
        NOT_IN_WHITE_LIST = -409
        JUDGER_ALREADY_AFFIRM = -410
        FORBIDDEN_ERROR = -411
        REDIS_EXEC_ERROR = -412
        NOT_ALLOWED_LOGIN_IN_GAME = -413
        ERROR_GATE_TIMEOUT = -414
        ERROR_ENTER_TEAM = -415
        COMPETITION_STEAM_ID_USED = -5601
        COMPETITION_RANK_SCORE_NOT_MATCH = -5602
        GAME_IS_ALREADY_LOCKED = -5603
        ERROR_IS_CREATING = -5604
        ERROR_TEAM_EXIST = -5605
        ERROR_PLAYER_MINORS = -5606
        ERROR_IN_BANNED_LIST = -5607

    class ServiceType(IntEnum):
        CLIENT = 0
        LOGIN_SERVER = 5000
        GATE_SERVER = 5100
        GAME_SERVER = 5200
        CENTER_SERVER = 5300
        ONLINE_SERVER = 5300
        DBPROXY_SERVER = 5400
        GAME_MATCH = 5500
        DOTA_MATCH = 5500
        GAME_SCORE = 5600
        DOTA_SCORE = 5600
        TEMP_TEAM_SERVER = 5700
        GROUP_SERVER = 5800
        NOTICE_SERVER = 5900
        DOTA2_HTML_SERVER = 6000
        GAME_SWITCH = 6100
        GAME_TEAM = 6200
        GAME_HONOUR = 6300
        DOTA2_DATA_IMPORT = 6400
        LOG_SERVER = 6500
        CSGO_MGR_SERVER = 6700
        CSGO_STATUS_SERVER = 6800
        WEB_PROXY = 6900
        FILTER = 7000
        WEB_GO_GATE = 7100
        ROBOT_SERVER = 7200
        CSGO_CUP_SERVER = 7300
        CSGO_MATCHING_SERVER = 7400
        CSGO_TOURNAMENT_SERVER = 7500
        FRIEND_SERVER = 7600
        CSGO_ENJOY_SERVER = 7700
        CSGO_PEAK_SERVER = 7800
        MSG_SYSTEM_SERVER = 7900
        CSGO_TRAINING_SERVER = 7950
        WEB_SOCIAL_SEVER = 8000
        DOTA2_CUP_SERVER = 8100
        DOTA2_PEAK_SERVER = 8200
        CSGO_SOLO_SERVER = 8300
        SOCIAL_PROXY_SERVER = 8400
        DOTA2_MATCHING_SERVER = 8500
        CSGO_TEAM_MATCHING_SERVER = 8600
        CSGO_APPOINT_GAME_SERVER = 8700
        MATCH_PASTIME_SERVER = 5509

    class GameType(IntEnum):
        DOTA = 1
        WAR3_1V1 = 2
        WAR3_2V2 = 3
        DOTA2 = 4
        IMBA = 5
        THIRD_SWORD = 6
        LZXF = 7
        CSGO = 8
        FILTER = 9
        AUTO_CHESS = 10

    class GameSlotType(IntEnum):
        SLOT_TYPE_ERROR = -128
        SLOT_TYPE_OB = -5
        SLOT_TYPE_COACH = -4
        SLOT_TYPE_JUDGER = -3
        SLOT_TYPE_B = -2
        SLOT_TYPE_A = -1
        SLOT_TYPE_NONE = 0
        SLOT_TYPE_1 = 1
        SLOT_TYPE_2 = 2
        SLOT_TYPE_3 = 3
        SLOT_TYPE_4 = 4
        SLOT_TYPE_5 = 5
        SLOT_TYPE_6 = 6
        SLOT_TYPE_7 = 7
        SLOT_TYPE_8 = 8
        SLOT_TYPE_9 = 9
        SLOT_TYPE_10 = 10
        SLOT_TYPE_99 = 99
    
    class LognameType(IntEnum):
        AUTO = 0
        USER_ID = 1
        USER_NAME = 2
        EMAIL = 3
        MOBILE_PHONE = 4
        PASSPORT = 5

    class NetworkLine(IntEnum):
        UNKNOW = 0
        CHINA_TELECOM = 1
        CHINA_UNICOM = 2
        EDUCATION_NETWORK = 4
        CHINA_MOBILE = 8
        MULTI_NETWORK = 65535

    class Dota2NetworkLine(IntEnum):
        NONE = 0
        CHINA_TC_SHANGHAI = 1
        CHINA_TC_ZHENJIANG = 2
        CHINA_TC_WUHAN = 4
        CHINA_TC_GUANGDONG = 8
        CHINA_UC = 16
        CHINA_UC2 = 32

    class IMOnlineStatus(IntEnum):
        OFFLINE = 0
        ONLINE = 1
        BUSY = 2
        AWAY = 4
        INVISIBLE = 8
        DISCONNECT = 16
        IN_TEMP_TEAM = 32
        IN_MATCH_GAME = 64
        IN_GAME = 128

    class IMFindType(IntEnum):
        LOGNAME = 1
        NICKNAME = 2

    class ReceiverType(IntEnum):
        USER = 1
        TEAM = 2
        GUILD = 4
        SCHOOL = 8
        TEMP_TEAM = 16
        TEMP_GROUP = 32
        FIX_GROUP = 64

    class IMFriendType(IntEnum):
        BLACK_LIST = 0
        UNCONFIRMED = 1
        FRIEND = 2
        TEMP_GROUP_MEMBER = 3
        FIXED_GROUP_MEMBER = 4

    class IMGender(IntEnum):
        UNKNOW = 0
        MALE = 1
        FEMALE = 2
        SECRET = 3

    class IMInviteType(IntEnum):
        JOIN_TEMP_GROUP = 1
        JOIN_FIXED_GROUP = 2
        JOIN_TEMP_TEAM = 3
        JOIN_FIXED_TEAM = 4
        JOIN_GUILD = 5
        JOIN_SCHOOL = 6
        OTHER = 250

    class IMChatType(IntEnum):
        PUBLIC_CHAT = 1
        AUTO_REPLY = 2
        USER_MOOD = 4
        POKE = 8
        SHAKE_WINDOW = 16

    class IMGroupRole(IntEnum):
        NORMAL = 1
        MANAGER = 2
        OWNER = 4

    class IMReplyResult(IntEnum):
        REFUSE = 0
        ACCEPT = 1

    class IMJoinRequestProcessResult(IntEnum):
        REQUESTING = -1
        REFUSE = 0
        ACCEPT = 1
        CANCEL = 2
        REMOVE = 3

    class DataStatus(IntEnum):
        INVALID = 0
        VALID = 1

    class GameScoreScopeType(IntEnum):
        USER = 1
        TEAM = 2
        GUILD = 4
        SCHOOL = 8
        CUP = 16
        AVE_COM = 32
        AVE_RANK = 64
        D2GOD_COM = 128
        D2GOD_RANK = 256
        COMPETITION = 257

    class GameSourceType(IntEnum):
        BEGIN_NUMBER = 1
        NORMAL = 1
        TEAM = 2
        ROOM = 3
        CUP = 4
        AVE = 5
        END_NUMBER = 10

    class GameMatchMode(IntEnum):
        AUTO = 1
        TEMP_TEAM = 2
        TEAM = 4

    class GameMode(IntEnum):
        AP = 1
        RD = 2
        SP = 4
        CM = 8
        DM = 16
        TR = 32
        SOLO = 64

    class ServiceStatus(IntEnum):
        DISABLED = 0
        ENABLED = 1
        LOCKED = 2

    class GameStatus(IntEnum):
        UNKNOW = 0
        WAIT = 1
        LOCK = 2
        ROBOT_HOST = 4
        CLIENT_HOST = 8
        READY = 16
        CREATE = 32
        LOADED_MAP = 64
        START = 128
        STOP = 256
        EXIT = 512

    class PlayeStatus(IntEnum):
        UNKNOW = 0
        WAIT_GAME = 1
        ENTER_GAME = 2
        PLAY_GAME = 4
        LEAVE_GAME = 8
        RESERVED_SLOT = 16
        MATCH_COMPLETED = 32

    class GameSlotStatus(IntEnum):
        CLOSED = 0
        OPENED = 1
        ASSIGNED = 2
        OCCUPIED = 4
        RESERVED = 8

    class KickType(IntEnum):
        KICK_OUT = -200
        TIME_OUT = -201
        OTHER_LOGIN = -202
        SERVICE_UNAVAILIABL = -203

    class CommDota2State(IntEnum):
        STATE_UNKONW = 0
        STATE_TO_LOAD = 1
        STATE_HERO_SELECTION = 2
        STATE_PRE_GAME = 3
        STATE_IN_PROGRESS = 4
        STATE_POST_GAME = 5
        STATE_DISCONNECT = 6

    class GameServiceCheckMode(IntEnum):
        NOT_CHECK = 0
        ONE_CHECK = 1
        TWO_CHECK = 2

    class GameReadyMode(IntEnum):
        NOT_READY_MODE = 0
        CAPTAIN_MODE = 1
        PLAYER_MODE = 2

    class CompetitionType(IntEnum):
        DPL = 1

    class CupMatchType(IntEnum):
        CMT_NORMAL_CUP = 0
        CMT_CSGO_PROFESSIONAL = 1
        CMT_CSGO_NET_BAR = 2
        CMT_CSGO_NET_BAR_TEAM = 3
        CMT_CSGO_NET_BAR_SPY = 4
        CMT_OFFLINE_1V1 = 5

    class CSGORollMapMode(IntEnum):
        NONE = 0
        SINGLE_MAP = 1
        RANDOM_MAP = 2
        BANPICK_MAP = 3
        MAX_MAP_NUMBER = 4

    class CSGOGameMode(IntEnum):
        GAME_MODE_COMPETITIVE = 1
        GAME_MODE_CASUAL = 2
        GAME_MODE_DEMOLITION = 3
        GAME_MODE_ARMS_RACE = 4
        GAME_MODE_DEATH_MATCH = 5

    class CSGOMapType(IntEnum):
        MAP_TYPE_RANDOM = 0
        MAP_TYPE_1V1_GUN = 1
        MAP_TYPE_1V1_AWP = 2
        MAP_TYPE_1V1_PISTOL = 3
        MAP_TYPE_1V1_KNIFE = 4
        MAP_TYPE_HIDESEEK = 5
        MAP_TYPE_DEATH_MATCH = 6
        MAP_TYPE_ZOMBIE_ESCAPE = 7
        MAP_TYPE_ZOMBIE_SUBWAY_ZWD = 8
        MAP_TYPE_ICE_WORLD = 9
        MAP_TYPE_RETAKE = 10
        MAP_TYPE_TEAM_DEATH_MATCH = 11
        MAP_TYPE_TEAM_CASUAL = 12
        MAP_TYPE_TEAM_1V1_GUN_MATCH = 13
        MAP_TYPE_GUN_TRAINING = 14
        MAP_TYPE_LAUNCH_TEST = 15
        MAP_TYPE_CSGO_UPDATE_NOTIFY = 16
        MAP_TYPE_COUNT = 17

    class CSGOMatchType:
        MATCH_TYPE_START = 10
        MATCH_TYPE_CUP = 10
        MATCH_TYPE_SOLO = 11
        MATCH_TYPE_RANK_MATCH = 12
        MATCH_TYPE_SPEED_MATCH = 13
        MATCH_TYPE_CUSTOM_MATCH = 14
        MATCH_TYPE_ENJOY_MATCH = 15
        MATCH_TYPE_NET_BAR = 16
        MATCH_TYPE_MATCH_BACKUP_1 = 17
        MATCH_TYPE_MATCH_BACKUP_2 = 18
        MATCH_TYPE_NET_BAR_DEATH = 19
        MATCH_TYPE_PRE_MATCH = 20
        MATCH_TYPE_CHESS_CUP = 21
        MATCH_TYPE_CUP_SPEED_MATCH = 22
        MATCH_TYPE_DOUBLE_MATCH = 23
        MATCH_TYPE_DOUBLE_CUP_SPEED_MATCH = 24
        MATCH_TYPE_DOUBLE_CUP = 25
        MATCH_TYPE_DOTA2_NET_BAR = 26
        MATCH_TYPE_WEEKEND_TOURNAMENT = 27
        MATCH_TYPE_ENJOY_DEFENSE = 28
        MATCH_TYPE_ENJOY_1V1 = 29
        MATCH_TYPE_ENJOY_TRAINING = 30
        MATCH_TYPE_ENJOY_DOD = 31
        MATCH_TYPE_ENJOY_SCIENTIFIC = 32
        MATCH_TYPE_MEET_WAR = 33
        MATCH_TYPE_1V1_MODE = 34
        MATCH_TYPE_ENJOY_1V1_PRO = 35
        MATCH_TYPE_DOTA2_PEAK = 36
        MATCH_TYPE_RED_PACKET = 37
        MATCH_TYPE_RANK_SOLO = 38
        MATCH_TYPE_DOTA2_YOULANG = 39
        MATCH_TYPE_TEAM_MATCHING = 40
        MATCH_TYPE_ORDINARY_MATCHING = 41
        MATCH_TYPE_RANK_CS2 = 42
        MATCH_TYPE_THIRD_PARTY = 43
        MATCH_TYPE_PEAK_SOLO = 44
        MATCH_TYPE_APPOINT_GAME = 45
        MATCH_TYPE_RANK_SINGLE = 46
        MATCH_TYPE_RANK_DL = 47
        MATCH_TYPE_CSGO_WORKSHOP = 48
        MATCH_TYPE_COUNT = 49

    class CSGOHostType(IntEnum):
        HOST_TYPE_TEAM = 0
        HOST_TYPE_1V1 = 1
        HOST_TYPE_HIDESEEK = 2
        HOST_TYPE_DEATH_MATCH = 3
        HOST_TYPE_ZOMBIE_ESCAPE = 4
        HOST_TYPE_ICE_WORLD = 5
        HOST_TYPE_RETAKE = 6
        HOST_TYPE_TEAM_DEATH_MATCH = 7
        HOST_TYPE_TEAM_CASUAL = 8
        HOST_TYPE_TEAM_1V1 = 9
        HOST_TYPE_GUN_TRAINING = 10
        HOST_TYPE_LAUNCH_TEST = 11
        HOST_TYPE_CSGO_UPDATE_NOTIFY = 12
        HOST_TYPE_COUNT = 13

    class GameOverType(IntEnum):
        NORMAL = 0
        ABANDON = 1
        JUDGEMENT = 2
    
    class CSGOGameOverReason(IntEnum):
        GAMEOVER_NORMAL = 0
        GAMEOVER_ROOM_RECREATE = 1
        GAMEOVER_ROOM_REMOVED = 2
        GAMEOVER_HOST_REMOVED = 3
        GAMEOVER_STATE_INVALID = 4
        GAMEOVER_CSGODUMP = 5
        GAMEOVER_NOTALLCONENCT = 6
        GAMEOVER_PLAYERBAN = 7
        GAMEOVER_ALLDISCONNECT = 8
        GAMEOVER_SURRENDER = 9
        GAMEOVER_PLAYERBANINWARMUP = 10
        GAMEOVER_ABANDON = 11
        GAMEOVER_ESCAPE = 12
        GAMEOVER_NEWBIEABNORMAL = 13
        GAMEOVER_MATCHBAN = 14
        GAMEOVER_ALLGIVEUP = 15
        GAMEOVER_PLAYERKICKBYADMIN = 16

    class DOTA_GameMode(IntEnum):
        DOTA_GAMEMODE_NONE = 0
        DOTA_GAMEMODE_AP = 1
        DOTA_GAMEMODE_CM = 2
        DOTA_GAMEMODE_RD = 3
        DOTA_GAMEMODE_SD = 4
        DOTA_GAMEMODE_AR = 5
        DOTA_GAMEMODE_INTRO = 6
        DOTA_GAMEMODE_HW = 7
        DOTA_GAMEMODE_REVERSE_CM = 8
        DOTA_GAMEMODE_XMAS = 9
        DOTA_GAMEMODE_TUTORIAL = 10
        DOTA_GAMEMODE_MO = 11
        DOTA_GAMEMODE_LP = 12
        DOTA_GAMEMODE_POOL1 = 13
        DOTA_GAMEMODE_FH = 14
        DOTA_GAMEMODE_CUSTOM = 15
        DOTA_GAMEMODE_CD = 16
        DOTA_GAMEMODE_BD = 17
        DOTA_GAMEMODE_ABILITY_DRAFT = 18
        DOTA_GAMEMODE_EVENT = 19
        DOTA_GAMEMODE_ARDM = 20
        DOTA_GAMEMODE_1V1MID = 21
        DOTA_GAMEMODE_ALL_DRAFT = 22
        DOTA_GAMEMODE_TURBO = 23

    class RegionId(IntEnum):
        US_WEST = 1
        US_EAST = 2
        EUROPE = 3
        SINGAPORE = 5
        DUBAI = 6
        AUSTRALIA = 7
        STOCKHOLM = 8
        AUSTRIA = 9
        BRAZIL = 10
        SOUTHAFRICA = 11
        PW_TELECOM_SHANGHAI = 12
        PW_UNICOM = 13
        CHILE = 14
        PERU = 15
        INDIA = 16
        PW_TELECOM_GUANGDONG = 17
        PW_TELECOM_ZHEJIANG = 18
        PW_TELECOM_WUHAN = 20
        PW_UNICOM_TIANJIN = 25

    class ZzqServerType(IntEnum):
        SPECIAL_SERVER = 1
        ALL_REGION_SERVER = 2
        STANDARD_REGION_SERVER = 3
        SERVER_TYPE_COUNT = 4
        
