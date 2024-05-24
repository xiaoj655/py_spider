class Config():
    mongodb_host:        str = 'mongodb://172.30.64.1:27017/'
    db_name:            str = 'weibo'
    uid:                list = ['1858002662']
    max_page:           int = 100
    cookie:             str ='_T_WM=04a3dcf959028bb13773aae2a2e49226; MLOGIN=0; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803; SCF=Ao6Q0sxK275VShrNRMSAllQII2bDMWJA1z2YynX3MuA3D6wMGQ4w8tVXideENyJrwDH30w3gtcEmANVzbfgqR70.; SUB=_2A25LVLPvDeRhGeFH6VAY9C_FzTiIHXVoKEknrDV6PUJbktAGLWqjkW1Ne6RgxwoYlid88p-dvgO_9uE-rtCIiOcL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-xwH7-1A2OihRyU1GzXTR5NHD95QN1KzE1KBp1KqXWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.Eeo.XeK.cS5tt; SSOLoginState=1716569024; ALF=1719161024'
    user_agent:         str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

    def get_headers(self):
        return {
            "Cookie": self.cookie,
            "User-Agent": self.user_agent
        }

cfg = Config()