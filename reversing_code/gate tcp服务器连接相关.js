function (e, t, r) {
      const i = r(372),
        s = r(10),
        a = r(11),
        n = r(704),
        o = r(8),
        u = r(183),
        p = r(705),
        c = r(138),
        m = r(232),
        l = r(706),
        d = r(26),
        y = r(707),
        h = r(97),
        _ = r(2705),
        g = r(2706),
        S = r(2707),
        b = r(230),
        T = r(2795),
        f = r(2798),
        I = r(2800),
        E = r(327),
        N = r(2803),
        A = r(257),
        k = r(20),
        { ipcMain: v, session: R } = r(2),
        C = r(54),
        w = r(271),
        D = r(114),
        M = r(58),
        x = global.logger.wslogin,
        P = r(84),
        F = r(23),
        q = r(29);
      let L = r(13),
        O = !1;
      function B(e, t = "", r = 0, i = 0) {
        0 == e
          ? !0 === h.reconnecting
            ? (h.notify_loginState(c.LoginState.Reconnect_Suc),
              setTimeout(() => {
                F.onReconnected();
              }, 100))
            : (h.notify_loginState(c.LoginState.Success),
              setTimeout(() => {
                _.reportNickname();
              }, 100),
              x.trace("============= 执行login"),
              F.onLogin())
          : (_.destroyClient(!0),
            (h.login_ErrCode = e),
            (h.error_text = t),
            (h.ban_type = r),
            (h.ban_expire_time = i),
            h.notify_loginState(c.LoginState.Failed));
      }
      let G = 0;
      function U(e) {
        let t = null == e ? o.ErrorCode.UNKOWN_ERROR : e.error_code;
        if (0 != t)
          return (
            x.error(
              "login failed you should return login window and try again later, err=" +
                t,
            ),
            void B(e.error_code, e.error_text, e.ban_type, e.ban_expire)
          );
        let r = e.user_info;
        h.session_ticket = e.session_ticket;
        let a = e.gate_list;
        if (a.length > 0 && 0 === e.error_code) {
          a.length <= G && (G = 0);
          let t = a[G];
          G++,
            (h.user_type = e.user_type),
            (h.gate_ip = t.service_ip),
            (h.gate_port = t.service_port);
          let o = i.HexAesDecrypt(r, i.aesKey[h.client_random].slice(0, 16)),
            u = s.deserializeBinary(
              Buffer.from(o, "binary"),
              n.ClientLoginResUserInfo,
            );
          (h.session_key = u.session_key),
            (L.id = h.user_id = u.user_id),
            (L.login_type = h.login_type),
            (h.connect_login_suc = !0),
            _.destroyClient(!1);
        }
      }
      function V(e, t) {
        let r = new a();
        switch (
          (r.deserialize(e),
          x.trace("recv login server msg_type:" + r.type),
          r.type)
        ) {
          case o.MessageType.MT_HELLO_NOTIFY:
            {
              x.trace("recv login hello notify");
              const e = s.deserializeBinary(t, o.HelloNotify);
              switch (((h.server_random = e.server_random), h.login_type)) {
                case c.LoginType.TOKEN:
                  x.trace("login by token: ", h.login_token),
                    _.send_client_token_req();
                  break;
                case c.LoginType.STEAMID:
                  x.trace("login by steam id"), _.send_client_steam_req();
                  break;
                default:
                  x.trace("unsupport login type.");
              }
            }
            break;
          case n.MessageType.MT_LOGIN_STATUS_NOTF:
            {
              const e = s.deserializeBinary(t, n.LoginStatusNotf);
              x.trace("MT_LOGIN_STATUS_NOTF: ", JSON.stringify(e)),
                1 === e.status &&
                  (k.setLoginTimeoutTimer(!1),
                  global.win.webContents.send("login-wait-in-queue-notify", e));
            }
            break;
          case n.MessageType.MT_CLIENT_TOKEN_LOGIN_RES:
            {
              let e = s.deserializeBinary(t, n.ClientLoginRes);
              x.trace("recv login res by token:", e.error_code), U(e);
            }
            break;
          case n.MessageType.MT_CLIENT_STEAM_LOGIN_RES:
            {
              let e = s.deserializeBinary(t, n.ClientLoginRes);
              x.trace("recv login res by steam id:", e), U(e);
            }
            break;
          default:
            x.trace("recv a unhanded msg", r.type);
        }
      }
      function j(e, t) {
        let i = new a();
        switch (
          (i.deserialize(e),
          (h.recv_data_time = process.uptime()),
          [
            u.MessageType.MT_KEEPLIVE_TEST_RES,
            o.MessageType.MT_KEEPALIVE_RES,
          ].includes(i.type) || x.trace("recv gate msg, type:" + i.type),
          i.type)
        ) {
          case o.MessageType.MT_HELLO_NOTIFY:
            {
              const e = s.deserializeBinary(t, o.HelloNotify);
              A.setTime(Number(e.server_time)),
                x.trace("recv gate hello notify " + e.server_time),
                (h.server_random = e.server_random),
                global.win.webContents.send(
                  "login-servertime-notify",
                  e.server_time,
                ),
                _.send_connect_req();
            }
            break;
          case u.MessageType.MT_CONNECT_RES:
            {
              const e = s.deserializeBinary(t, u.ConnectRes);
              0 === e.error_code
                ? (x.trace("recv connect res suc, local ip: ", e.error_text),
                  (h.encrypt_socket_ = !0),
                  (h.login_suc = !0),
                  _.setkeepaliveTimer(),
                  e.error_text &&
                    e.error_text.match(/^(\d+).(\d+).(\d+).(\d+)$/g) &&
                    ((L.ipAddr = e.error_text), (e.error_text = "")))
                : x.trace("recv connect res error, need relogin"),
                B(e.error_code, e.error_text),
                global.win.webContents.send("sys-notice-notify", {
                  type: 59,
                  content: JSON.stringify({
                    is_opened: e.shield_nonrank_entrance_switch,
                  }),
                });
            }
            break;
          case p.MessageType.MT_KICK_LOGOUT_NOTIFY:
            {
              const e = s.deserializeBinary(t, p.OnlineKickLogoutNotify);
              x.trace("recv a kicked logout notify", e),
                k.disconnect(() => {
                  (h.kick_info = { by: "client", reason: 0 }),
                    h.notify_loginState(c.LoginState.kicked);
                }),
                global.game.csgo && global.game.csgo.killCs2(),
                global.win && global.win.show();
            }
            break;
          case p.MessageType.MT_KICK_MINORS_NOTF:
            {
              const e = s.deserializeBinary(t, p.KickMinorsNotf);
              global.win.webContents.send("CSGO_COMMON_KICK_MINORS_NOTIFY", e);
            }
            break;
          case y.MessageType.MT_WEB_KICKOUT_USER_NOTIFY:
            {
              const e = s.deserializeBinary(t, y.WebKickoutUserNotify);
              x.trace("rece web kickout user notify", e),
                k.disconnect(() => {
                  (h.kick_info = { by: "web", reason: e.kick_reason }),
                    h.notify_loginState(c.LoginState.kicked);
                });
            }
            break;
          case p.MessageType.MT_PLATFORM_MAINTAINS_NOTIFY:
            {
              const e = s.deserializeBinary(t, p.OnlinePlatformMaintainsNotify);
              x.trace("recv a platform maintains notify : " + JSON.stringify(e)),
                k.disconnect(() => {
                  global.win.webContents.send("platform-maintain-notify", e);
                });
            }
            break;
          case P.MessageType.MT_CSGO_USER_MESSAGE_NOTIFY:
            {
              const r = s.deserializeBinary(t, P.CsgoUserMessageNotify);
              if (
                (x.trace("recv a csgo user message notify", r),
                F.csgoMessageNotify(r),
                1001 == r.cmd_id)
              )
                w(r, "/resources/app.asar/html/static/html/test.html");
              else if (1002 == r.cmd_id)
                try {
                  const { starter: e = "", towho: t = "" } = JSON.parse(
                    r.message,
                  );
                  global.win.webContents.send(
                    "CSGO_LADDER_GRUDGE_MATCH_MT_CHALLENGE_NOTF",
                    { challenge_id: e },
                  );
                } catch (e) {}
              else if (1003 == r.cmd_id);
              else if (1004 == r.cmd_id);
              else if (100 == r.cmd_id) {
                x.trace("recv a csgo kick out notify", r);
                try {
                  const { kick_reason: e, is_show: t } = JSON.parse(r.message);
                  t &&
                    e &&
                    global.win.webContents.send("user_kick_out_notify", e);
                } catch (e) {}
              } else if (102 == r.cmd_id) {
                x.trace("recv a csgo workshop training map downloaded notify", r);
                try {
                  const e = JSON.parse(r.message);
                  global.win.webContents.send("WORKSHOP_TRAIN_MAP_DOWNLOADED", e);
                } catch (e) {}
              }
            }
            break;
          case q.MessageType.MT_GET_LAUNCH_TEST_INFO_RES:
            {
              const e = s.deserializeBinary(t, q.GetLaunchTestInfoRes);
              x.trace("recv a csgo check ingo res", e), F.csgoCheckInfoRes(e);
            }
            break;
          case P.MessageType.MT_GAMEOVER_DISCONNECT_NOTIFY:
            {
              const e = s.deserializeBinary(t, P.GameoverDisconnectNotify);
              x.trace("recv a MT_GAMEOVER_DISCONNECT_NOTIFY", e),
                F.csgoGameoverDisconnectNotify(e);
            }
            break;
          case d.MessageType.MT_SYS_NOTICE_MSG_NOTIFY:
            {
              const i = s.deserializeBinary(t, d.SysNoticeMsg);
              if ((x.trace("recv a sys notice notify", i), 11 === i.type));
              else if (15 === i.type)
                console.log("receive upload log notice：", i),
                  r(612).uploadLog((e) => {
                    console.log("upload log complete");
                  });
              else if (39 === i.type || 38 === i.type)
                x.trace("recv a sys notice notify sendAll", i.type),
                  D.setStorage("reportReady", i),
                  C.sendWindow("report", "sys-notice-notify", i);
              else if (48 === i.type)
                try {
                  const e = (JSON.parse(i.content) || []).some(
                      (e) => "CSGO" === e.game_abbr && "1" == e.forbid_type,
                    )
                      ? 1
                      : 0,
                    t = { msg_id: "USER_FORBID_STATE", steamId: L.id, state: e };
                  M.sendJsonMessage(JSON.stringify(t));
                } catch (e) {}
              global.win.webContents.send("sys-notice-notify", i);
            }
            break;
          case d.MessageType.MT_PLATFORM_UPDATE_NOTF:
            {
              let e = s.deserializeBinary(t, d.PlatformUpdateNotf);
              x.trace("recv a platform update notf", e),
                global.win.webContents.send("platform-update-notf", e);
            }
            break;
          case u.MessageType.MT_KEEPLIVE_TEST_RES:
            break;
          case o.MessageType.MT_KEEPALIVE_RES:
            h.recv_keepalive_res_time = process.uptime();
            break;
          case p.MessageType.MT_USER_INFO_REPORT_RES:
            {
              let e = s.deserializeBinary(t, p.UpdateUserBaicInfoRes);
              console.log("recv update user info res: ", e),
                x.trace("recv update user info res: ", e);
            }
            break;
          case p.MessageType.MT_BATCH_GET_USER_INFO_RES:
            {
              let e = s.deserializeBinary(t, p.BatchGetUserInfoRes);
              console.log("MT_BATCH_GET_USER_INFO_RES: ", e),
                x.trace("MT_BATCH_GET_USER_INFO_RES: ", e),
                global.win.webContents.send(
                  g.ResType.MT_BATCH_GET_USER_INFO_RES,
                  e,
                ),
                C.sendAll(g.ResType.MT_BATCH_GET_USER_INFO_RES, e);
            }
            break;
          default:
            i.type == d.MessageType.MT_INFO_CENTER_MSG_NOTIFY
              ? f.handle_Center_MsG(e, t)
              : i.type > m.MessageType.MT_SYNC_LINE &&
                  i.type < m.MessageType.MT_END_NUMBER
                ? b.handle_IM_Msg(e, t)
                : i.type > l.MessageType.MT_BEGIN_NUMBER &&
                    i.type < l.MessageType.MT_END_NUMBER
                  ? T.handle_response(e, t)
                  : i.type > E.MessageType.MT_BEGIN_NUMBER &&
                      i.type < E.MessageType.MT_END_NUMBER
                    ? I.handle_msg_system_response(e, t)
                    : i.type > q.MessageType.MT_CHANNEL_PROTOCOL_BEGIN &&
                        i.type <= q.MessageType.MT_CHANNEL_PROTOCOL_END
                      ? N.handle_response(e, t)
                      : S.handle_matchMsg(e, t);
        }
      }
      e.exports = class {
        static ipcListen() {
          1 != O &&
            ((O = !0),
            console.log(
              "login_api_types.ReqType.MT_BATCH_GET_USER_INFO_REQ",
              g.ReqType.MT_BATCH_GET_USER_INFO_REQ,
            ),
            v.on(g.ReqType.MT_BATCH_GET_USER_INFO_REQ, (e, t) => {
              console.log("LOGIN:  batchUserInfo, " + JSON.stringify(t)),
                x.trace("LOGIN:  batchUserInfo, " + JSON.stringify(t)),
                _.batchUserInfo(t);
            }));
        }
        static initModule(e) {
          var t;
          (t = e),
            b.connect(t),
            T.connect(),
            S.connect(t),
            f.connect(t),
            I.connect(t),
            N.connect(),
            this.ipcListen();
        }
        static connect(e, t, r, i) {
          (h.notify_win = i), _.connect(e, t, r, V, j);
        }
        static disconnect(e) {
          _.disconnect(e);
        }
      };
    },