function (e, t, r) {
      var i = r(27);
      r(174);
      var s = r(19),
        a = r(813);
      class n extends i.TBinaryProtocol {
        constructor(e, t, r) {
          super(e, t, r);
        }
        readI64() {
          return a.toDecimalString(super.readI64());
        }
        writeI64(e) {
          return super.writeI64(a.fromDecimalString(e));
        }
      }
      e.exports = class {
        static Bytes2HexString(e) {
          let t = "";
          for (let r = 0; r < e.length; r++) {
            let i = e[r].toString(16);
            1 === i.length && (i = "0" + i), (t += i.toUpperCase());
          }
          return t;
        }
        static Hexstring2btye(e) {
          let t = 0,
            r = e.length;
          if (r % 2 != 0) return null;
          r /= 2;
          let i = new Array();
          for (let s = 0; s < r; s++) {
            let r = e.substr(t, 2),
              s = parseInt(r, 16);
            i.push(s), (t += 2);
          }
          return i;
        }
        static writeUInt64BE(e, t, r) {
          return (
            void 0 === r ||
              0 === r ||
              "" === r ||
              a.fromDecimalString(r).toBuffer().copy(e, t),
            e
          );
        }
        static readUInt64BE(e, t) {
          var r = new s(e, t);
          return a.toDecimalString(r);
        }
        static serializeBinary(e) {
          let t;
          const r = new i.TBufferedTransport(null, function (e) {
              t = e;
            }),
            s = new n(r);
          return e.write(s), s.flush(), t;
        }
        static deserializeBinary(e, t) {
          const r = new i.TFramedTransport(e),
            s = new n(r),
            a = new t();
          return a.read(s), a;
        }
      };
    },

    var P = (e.exports.EnterTeamReq = function (e) {
      (this.team_id = null),
        (this.match_mode = null),
        (this.enter_channel = null),
        (this.grudge_team_id = null),
        e &&
          (void 0 !== e.team_id &&
            null !== e.team_id &&
            (this.team_id = e.team_id),
          void 0 !== e.match_mode &&
            null !== e.match_mode &&
            (this.match_mode = e.match_mode),
          void 0 !== e.enter_channel &&
            null !== e.enter_channel &&
            (this.enter_channel = e.enter_channel),
          void 0 !== e.grudge_team_id &&
            null !== e.grudge_team_id &&
            (this.grudge_team_id = e.grudge_team_id));
    });