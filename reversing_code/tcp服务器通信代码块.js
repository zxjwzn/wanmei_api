function (e, t, r) {
  const i = r(174),
    s = r(46),
    a = r(372),
    n = r(10),
    o = r(11),
    u = r(8),
    p = r(97),//login_info构造
    c = r(13),
    m = r(77),
    l = r(138),
    d = global.logger.wslogin,
    y = (r(183), r(14));
  let h = null,
    _ = null,
    g = 0,
    S = null,
    b = null;
  const T = Buffer.alloc(1048576);
  let f = 0;
  class I {
    static connect(e, t, i, a, n) {
      if (
        (N(!0),
        (b = new s.Socket()),
        b.setEncoding("binary"),
        (p.login_type = i),
        (p.user_id = t),
        "" === p.user_id)
      ) {
        const e = r(23);
        p.user_id = e.localSteamId64;
      }
      p.login_token = e;
      let u = m.getConfig().login_server,
        c = m.getConfig().login_port;
      p.notify_loginState(l.LoginState.Connecting),
      
        d.trace(
          `connect login server,ip=${u},port=${c},region=${m.getRegion()},login_type=${p.login_type},user_id=${p.user_id}`,
        ),
        A(!1),
        b.connect(c, u),//连接登录服务器，获取到登录凭据信息
        b.on("connect", function () {
          d.trace("login server connect sucessfully.");
          console.log("login_info from connect：", JSON.stringify(p));
        }),
        b.on("error", function (e) {
          d.error("login server socket error:" + e),
            !0 === p.connect_login_suc &&
              (d.trace("start connect gate"),
              clearTimeout(S),
              v(n),
              (p.connect_login_suc = !1));
        }),
        b.on("close", function (e) {
          d.error("login server socket close, err:" + e),
            !0 === p.connect_login_suc &&
              (d.trace("start connect gate"),
              clearTimeout(S),
              v(n),
              (p.connect_login_suc = !1));
        }),
        b.on("end", function (e) {
          d.error("login server socket end:" + e),
            !0 === p.connect_login_suc &&
              (d.trace("start connect gate"),
              clearTimeout(S),
              v(n),
              (p.connect_login_suc = !1));
        }),
        b.on("data", function (e) {//获取消息并解析
          console.log("login_info from data：", JSON.stringify(p));
          const t = Buffer.from(e, "binary"),
            r = t.length;
          if (f + r > 1048576)
            return (
              d.error(
                "接收缓冲区溢出，可能是消息分包出错，丢弃所有已接收到的消息",
              ),
              void (f = 0)
            );
          if ((t.copy(T, f), (f += r), f < o.head_size)) return;
          let i = T.readUInt32BE(0);
          for (; f >= i; ) {
            const headerBuffer = Buffer.from(T.slice(0, o.head_size));
            const bodyBuffer = Buffer.from(T.slice(o.head_size, i));
            console.warn(a.toString());
            a(
              headerBuffer,
              bodyBuffer,
            );//解析并构造登录session
            console.warn("headerBuffer",headerBuffer);
            console.warn("bodyBuffer",bodyBuffer);
            let e = f - i;
            if (e > 0) {
              let t = Buffer.alloc(e);
              T.copy(t, 0, i, f), t.copy(T, 0);
            }
            if (((f = e), f < o.head_size)) return;
            i = T.readUInt32BE(0);
          }
        });
    }
    static disconnect(e) {
      d.trace("-----destroy client,exit app!-----"),
        p.notify_loginState(l.LoginState.Disconnect),
        c.onLogout(),
        r(23).onLogout(),
        y.setTournamentState(0),
        N(!0),
        "function" == typeof e && e();
    }
    static user_id() {
      return p.user_id;//获取登录的用户id
    }
    static send_message(e, t) {
      if (p.login_suc) return R(e, t);
      d.trace("client is not logined, cann't send message at present");
    }
    static send_message_unauthorerd(e, t) {
      return R(e, t);
    }
    static destroyClient(e) {
      N(e);
    }
    static setkeepaliveTimer() {
      S && S.hasRef && clearTimeout(S),
        _ && _.hasRef && clearInterval(_),
        (h = setInterval(E, 1e4));
    }
    static setLoginTimeoutTimer(e) {
      A(e);
    }
  }
  function E() {
    const e = process.uptime();
    if (p.recv_data_time && e - p.recv_data_time > 60)
      return (
        d.error(
          `gate message timeout, need reconnect, uptime=${e}, recv_data_time=${p.recv_data_time}, recv_keepalive_res_time=${p.recv_keepalive_res_time}`,
        ),
        void b.destroy()
      );
    (e - p.recv_data_time > 18 || e - p.recv_keepalive_res_time > 36) &&
      (function () {
        let e = new o();
        (e.type = u.MessageType.MT_KEEPALIVE_REQ), (e.source = p.user_id);
        let t = new u.KeepAliveReq(),
          r = n.serializeBinary(t);
        e.length = o.head_size + r.length;
        let i = e.serialize();
        I.send_message(i, r);
      })();
  }
  function N(e) {
    d.trace(`destroy_client, recv_size = ${f}, clean_data = ${e}`),
      null != b && (b.destroy(), (b = null)),
      e &&
        (clearTimeout(S),
        p.data_init(),
        (p.client_random = (function (e, t) {
          const r = t - 0,
            s = i.random();
          return 0 + i.floor(s * r);
        })(0, a.aesKey.length)),
        d.trace("client random num: " + p.client_random),
        clearInterval(_),
        clearInterval(h),
        clearTimeout(S),
        (f = 0),
        (g = 0)),
      (f = 0);
  }
  function A(e) {
    clearTimeout(S),
      (S = null),
      (S = setTimeout(
        function (e) {
          (1 == e ? p.login_suc : p.connect_login_suc) ||
            (N(!0),
            (p.login_ErrCode = u.ErrorCode.ERROR_GATE_TIMEOUT),
            p.notify_loginState(l.LoginState.Failed));
        },
        e ? 2e4 : 8e4,
        e,
      ));
  }
  function k(e) {
    (p.encrypt_socket_ = !1),
      (p.reconnecting = !0),
      (g = 0),
      v(e),
      (_ = setInterval(v, 1e4, e));
  }
  function v(e) {
    N(!1),
      (b = new s.Socket()),
      b.setEncoding("binary"),
      !0 === p.reconnecting
        ? (d.trace("re-connect gate,retry-times=" + ++g),
          p.notify_loginState(l.LoginState.ReConnecting))
        : (d.trace("connect gate"), A(!0)),
      b.connect(p.gate_port, p.gate_ip),
      b.on("connect", function () {
        d.trace("gate server established connect.");
      }),
      b.on("error", function (t) {
        d.error("gate server socket error:" + t),
          1 == p.login_suc && ((p.login_suc = !1), clearInterval(h), k(e));
      }),
      b.on("close", function (t) {
        d.error("gate server socket close, err:" + t),
          1 == p.login_suc && ((p.login_suc = !1), clearInterval(h), k(e));
      }),
      b.on("end", function (t) {
        d.error("gate server socket end, error:" + t),
          1 == p.login_suc && ((p.login_suc = !1), clearInterval(h), k(e));
      }),
      b.on("data", function (t) {
        const r = Buffer.from(t, "binary"),
          i = r.length;
        if (f + i > 1048576)
          return (
            d.error(
              "接收缓冲区溢出，可能是消息分包出错，丢弃所有已接收到的消息",
            ),
            void (f = 0)
          );
        if ((r.copy(T, f), (f += i), f < o.head_size)) return;
        let s = T.readUInt32BE(0);
        for (; f >= s; ) {
          if (p.encrypt_socket_) {
            let t = Buffer.from(T.slice(4, s)),
              r = a.PVPDecrypt(t, p.session_key),
              i = Buffer.from(r, "binary"),
              n = i.readUInt32BE(0);
            console.warn("login_info", JSON.stringify(p));
            e(
              Buffer.from(i.slice(0, o.head_size)),
              Buffer.from(i.slice(o.head_size, n)),
            );
          } else
            e(
              Buffer.from(T.slice(0, o.head_size)),
              Buffer.from(T.slice(o.head_size, s)),
            );
          let t = f - s;
          if (t > 0) {
            let e = Buffer.alloc(t);
            T.copy(e, 0, s, f), e.copy(T, 0);
          }
          if (((f = t), f < o.head_size)) return;
          s = T.readUInt32BE(0);
        }
      });
  }
  function R(e, t) {
    if (null == b || b.destroyed)
      return void d.trace(
        "client cannot be null or destroyed,you cannot send message at present.",
      );
    let r = Buffer.alloc(e.length + t.length);
    if ((e.copy(r, 0), t.copy(r, o.head_size), p.encrypt_socket_)) {
      let e = a.PVPEncrypt(r, p.session_key),
        t = e.length + 4,
        i = Buffer.alloc(t);
      i.writeUInt32BE(t, 0), Buffer.from(e).copy(i, 4), b.write(i);
    } else b.write(r);
  }
  e.exports = I;
},
function (e, t, r) {
  "use strict";
  Object.defineProperty(t, "__esModule", { value: !0 }),
    (t.checkBucketName = void 0),
    (t.checkBucketName = (e, t = !1) => {
      if (
        !(
          t
            ? /^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$/
            : /^[a-z0-9_][a-z0-9-_]{1,61}[a-z0-9_]$/
        ).test(e)
      )
        throw new Error("The bucket must be conform to the specifications");
    });
},