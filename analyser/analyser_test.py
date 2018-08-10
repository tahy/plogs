import pytest
import uuid

@pytest.fixture
def test_file():

	test_log = """
Jul 10 10:09:04 srv24-s-st postfix/smtpd[4703]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:04 srv24-s-st postfix/smtpd[4703]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:04 srv24-s-st postfix/smtpd[16079]: lost connection after AUTH from unknown[116.11.27.165]
Jul 10 10:09:04 srv24-s-st postfix/smtpd[16079]: disconnect from unknown[116.11.27.165]
Jul 10 10:09:05 srv24-s-st postfix/smtpd[10344]: disconnect from m90-138-113-58.cust.tele2.ru[90.138.113.58]
Jul 10 10:09:06 srv24-s-st postfix/smtpd[11171]: warning: unknown[183.7.120.155]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:06 srv24-s-st postfix/smtpd[16080]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:06 srv24-s-st postfix/smtpd[16080]: connect from unknown[178.140.204.161]
Jul 10 10:09:06 srv24-s-st postfix/smtpd[11171]: lost connection after AUTH from unknown[183.7.120.155]
Jul 10 10:09:06 srv24-s-st postfix/smtpd[11171]: disconnect from unknown[183.7.120.155]
Jul 10 10:09:07 srv24-s-st postfix/smtpd[16077]: warning: unknown[61.141.72.43]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:07 srv24-s-st postfix/smtpd[10344]: connect from unknown[183.7.120.155]
Jul 10 10:09:07 srv24-s-st postfix/smtpd[16077]: lost connection after AUTH from unknown[61.141.72.43]
Jul 10 10:09:07 srv24-s-st postfix/smtpd[16077]: disconnect from unknown[61.141.72.43]
Jul 10 10:09:08 srv24-s-st postfix/smtpd[14197]: warning: unknown[222.218.152.89]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:08 srv24-s-st postfix/smtpd[16080]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:08 srv24-s-st postfix/smtpd[16080]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:08 srv24-s-st postfix/smtpd[16080]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:08 srv24-s-st postfix/smtpd[16079]: warning: 61.141.72.43: hostname 43.72.141.61.broad.sz.gd.dynamic.163data.com.cn verification failed: Name or service not known
Jul 10 10:09:08 srv24-s-st postfix/smtpd[16079]: connect from unknown[61.141.72.43]
Jul 10 10:09:08 srv24-s-st postfix/smtpd[14197]: lost connection after AUTH from unknown[222.218.152.89]
Jul 10 10:09:08 srv24-s-st postfix/smtpd[14197]: disconnect from unknown[222.218.152.89]
Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]: 25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>, size=617951, nrcpt=1 (queue active)
Jul 10 10:09:09 srv24-s-st postfix/smtp[23225]: EB3DCDF04EB: to=<arsenal@scn.ru>, relay=mail.scn.ru[80.255.139.141]:25, delay=65, delays=27/0/1.3/36, dsn=2.0.0, status=sent (250 OK id=1SoTaM-0007or-4a)
Jul 10 10:09:09 srv24-s-st postfix/qmgr[3043]: EB3DCDF04EB: removed
Jul 10 10:09:09 srv24-s-st postfix/smtpd[27067]: disconnect from unknown[213.87.122.107]
Jul 10 10:09:09 srv24-s-st postfix/smtp[22621]: 25E6CDF04F4: to=<arsenal-krsk@mail.ru>, relay=mxs.mail.ru[94.100.176.20]:25, delay=33, delays=32/0/0.01/0.76, dsn=2.0.0, status=sent (250 OK id=1SoTcj-0001fx-Bs)
Jul 10 10:09:09 srv24-s-st postfix/qmgr[3043]: 25E6CDF04F4: removed
Jul 10 10:09:10 srv24-s-st postfix/smtpd[27068]: 451CEDF04EB: client=unknown[213.87.122.107], sasl_method=LOGIN, sasl_username=manager30@moda-milena.ru
Jul 10 10:09:10 srv24-s-st postfix/smtpd[4703]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:10 srv24-s-st postfix/smtpd[4703]: connect from unknown[178.140.204.161]
Jul 10 10:09:12 srv24-s-st postfix/smtpd[10344]: warning: unknown[183.7.120.155]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:12 srv24-s-st postfix/smtpd[4703]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:12 srv24-s-st postfix/smtpd[16079]: warning: unknown[61.141.72.43]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:12 srv24-s-st postfix/smtpd[4703]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:12 srv24-s-st postfix/smtpd[4703]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:12 srv24-s-st postfix/smtpd[16079]: lost connection after AUTH from unknown[61.141.72.43]
Jul 10 10:09:12 srv24-s-st postfix/smtpd[16079]: disconnect from unknown[61.141.72.43]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[10344]: lost connection after AUTH from unknown[183.7.120.155]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[10344]: disconnect from unknown[183.7.120.155]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[16081]: warning: 81.177.6.31: address not listed for hostname srv24-s-st.jino.ru
Jul 10 10:09:13 srv24-s-st postfix/smtpd[16081]: connect from unknown[81.177.6.31]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[16081]: disconnect from unknown[81.177.6.31]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[10339]: warning: 61.141.72.43: hostname 43.72.141.61.broad.sz.gd.dynamic.163data.com.cn verification failed: Name or service not known
Jul 10 10:09:13 srv24-s-st postfix/smtpd[10339]: connect from unknown[61.141.72.43]
Jul 10 10:09:13 srv24-s-st postfix/cleanup[6471]: 451CEDF04EB: message-id=<20120710060910.451CEDF04EB@smtp.jino.ru>
Jul 10 10:09:13 srv24-s-st postfix/smtpd[10285]: connect from unknown[183.7.120.155]
Jul 10 10:09:13 srv24-s-st postfix/smtpd[11171]: connect from shpd-95-53-131-46.static.vologda.ru[95.53.131.46]
Jul 10 10:09:14 srv24-s-st postfix/smtpd[16077]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:14 srv24-s-st postfix/smtpd[16077]: connect from unknown[178.140.204.161]
Jul 10 10:09:16 srv24-s-st postfix/smtpd[16077]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:16 srv24-s-st postfix/smtpd[16077]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:16 srv24-s-st postfix/smtpd[16077]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:17 srv24-s-st postfix/smtpd[10339]: warning: unknown[61.141.72.43]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:17 srv24-s-st postfix/smtpd[10339]: lost connection after AUTH from unknown[61.141.72.43]
Jul 10 10:09:17 srv24-s-st postfix/smtpd[10339]: disconnect from unknown[61.141.72.43]
Jul 10 10:09:17 srv24-s-st postfix/smtpd[5486]: connect from n53-h187.gw-net.metromax.ru[81.22.53.187]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[10285]: warning: unknown[183.7.120.155]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:18 srv24-s-st postfix/smtpd[16080]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:18 srv24-s-st postfix/smtpd[16080]: connect from unknown[178.140.204.161]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[10339]: warning: 61.141.72.43: hostname 43.72.141.61.broad.sz.gd.dynamic.163data.com.cn verification failed: Name or service not known
Jul 10 10:09:18 srv24-s-st postfix/smtpd[10339]: connect from unknown[61.141.72.43]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[16079]: warning: 81.177.6.31: address not listed for hostname srv24-s-st.jino.ru
Jul 10 10:09:18 srv24-s-st postfix/smtpd[16079]: connect from unknown[81.177.6.31]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[16079]: disconnect from unknown[81.177.6.31]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[10285]: lost connection after AUTH from unknown[183.7.120.155]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[10285]: disconnect from unknown[183.7.120.155]
Jul 10 10:09:18 srv24-s-st postfix/smtpd[5486]: F1DB8DF04EF: client=n53-h187.gw-net.metromax.ru[81.22.53.187], sasl_method=PLAIN, sasl_username=oksana_b@kubometr-samara.ru
Jul 10 10:09:19 srv24-s-st postfix/cleanup[6537]: F1DB8DF04EF: message-id=<4FFBC6F0.2080809@kubometr-samara.ru>
Jul 10 10:09:19 srv24-s-st postfix/qmgr[3043]: F1DB8DF04EF: from=<oksana_b@kubometr-samara.ru>, size=11263, nrcpt=1 (queue active)
Jul 10 10:09:19 srv24-s-st postfix/smtpd[10344]: connect from unknown[183.7.120.155]
Jul 10 10:09:19 srv24-s-st postfix/smtpd[5486]: disconnect from n53-h187.gw-net.metromax.ru[81.22.53.187]
Jul 10 10:09:20 srv24-s-st postfix/smtp[22635]: F1DB8DF04EF: to=<ninachekmeneva@mail.ru>, relay=mxs.mail.ru[94.100.176.20]:25, delay=1.3, delays=0.76/0/0.02/0.49, dsn=2.0.0, status=sent (250 OK id=1SoTcu-0003aF-80)
Jul 10 10:09:20 srv24-s-st postfix/qmgr[3043]: F1DB8DF04EF: removed
Jul 10 10:09:20 srv24-s-st postfix/smtpd[16080]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:20 srv24-s-st postfix/smtpd[16080]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:20 srv24-s-st postfix/smtpd[16080]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:21 srv24-s-st postfix/smtpd[16081]: warning: 188.168.65.94: hostname 188.168.65.94.retail.sakhttk.ru verification failed: Name or service not known
Jul 10 10:09:21 srv24-s-st postfix/smtpd[16081]: connect from unknown[188.168.65.94]
Jul 10 10:09:21 srv24-s-st postfix/qmgr[3043]: 718F4DF04E9: from=<krasteplokomplekt@yandex.ru>, size=617940, nrcpt=1 (queue active)
Jul 10 10:09:21 srv24-s-st postfix/smtp[6782]: 718F4DF04E9: to=<arsenya08@mail.ru>, relay=mxs.mail.ru[94.100.176.20]:25, delay=21, delays=21/0/0.02/0.14, dsn=5.0.0, status=bounced (host mxs.mail.ru[94.100.176.20] said: 550 Message was not accepted -- invalid mailbox.  Local mailbox arsenya08@mail.ru is unavailable: user not found (in reply to end of DATA command))
Jul 10 10:09:21 srv24-s-st postfix/cleanup[8898]: D69F5DF04F4: message-id=<20120710060921.D69F5DF04F4@smtp.jino.ru>
Jul 10 10:09:21 srv24-s-st postfix/qmgr[3043]: D69F5DF04F4: from=<>, size=3104, nrcpt=1 (queue active)
Jul 10 10:09:21 srv24-s-st postfix/bounce[24126]: 718F4DF04E9: sender non-delivery notification: D69F5DF04F4
Jul 10 10:09:21 srv24-s-st postfix/qmgr[3043]: 718F4DF04E9: removed
Jul 10 10:09:21 srv24-s-st postfix/smtpd[16077]: warning: 178.46.158.31: hostname 31.158.access.ttknet.ru verification failed: Name or service not known
Jul 10 10:09:21 srv24-s-st postfix/smtpd[16077]: connect from unknown[178.46.158.31]
Jul 10 10:09:22 srv24-s-st postfix/smtp[22635]: D69F5DF04F4: host mx.yandex.ru[213.180.204.89] said: 451 4.7.1 Sorry, the service is currently unavailable. Please come back later. 8ohqT2RI-8ohqQZ6F (in reply to end of DATA command)
Jul 10 10:09:22 srv24-s-st postfix/smtp[22635]: D69F5DF04F4: to=<krasteplokomplekt@yandex.ru>, relay=mx.yandex.ru[213.180.193.89]:25, delay=0.26, delays=0/0/0.21/0.05, dsn=4.7.1, status=deferred (host mx.yandex.ru[213.180.193.89] said: 451 4.7.1 Sorry, the service is currently unavailable. Please come back later. 8o4KRFlt-8o4Kls3x (in reply to end of DATA command))
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16081]: 466CEDF04EF: client=unknown[188.168.65.94], sasl_method=CRAM-MD5, sasl_username=ecolog@midglengroup.ru
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16077]: 4E15ADF04FA: client=unknown[178.46.158.31], sasl_method=CRAM-MD5, sasl_username=777md@ugor.ru
Jul 10 10:09:22 srv24-s-st postfix/smtpd[10339]: warning: unknown[61.141.72.43]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16080]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16080]: connect from unknown[178.140.204.161]
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16077]: 4E15ADF04FA: reject: RCPT from unknown[178.46.158.31]: 550 5.1.1 <                            >: Recipient address rejected: User unknown in local recipient table; from=<777md@ugor.ru> to=<????????????????????????????> proto=ESMTP helo=<[192.168.0.58]>
Jul 10 10:09:22 srv24-s-st postfix/smtpd[10620]: disconnect from unknown[213.87.122.107]
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16081]: warning: Illegal address syntax from unknown[188.168.65.94] in RCPT command: <lazarev@dfgazflot.ru" <lazarev@dfgazflot.ru>, ???????????? ?????????? <tikhov@midglengroup.ru>">
Jul 10 10:09:22 srv24-s-st postfix/smtpd[16077]: disconnect from unknown[178.46.158.31]
Jul 10 10:09:22 srv24-s-st postfix/smtpd[4703]: connect from broadband-77-37-236-62.nationalcablenetworks.ru[77.37.236.62]
Jul 10 10:09:22 srv24-s-st postfix/smtpd[10339]: lost connection after AUTH from unknown[61.141.72.43]
Jul 10 10:09:22 srv24-s-st postfix/smtpd[10339]: disconnect from unknown[61.141.72.43]
Jul 10 10:09:23 srv24-s-st postfix/smtpd[16081]: disconnect from unknown[188.168.65.94]
Jul 10 10:09:23 srv24-s-st postfix/smtpd[4703]: 58189DF04EF: client=broadband-77-37-236-62.nationalcablenetworks.ru[77.37.236.62], sasl_method=LOGIN, sasl_username=ans@merchcenter.ru
Jul 10 10:09:23 srv24-s-st postfix/smtpd[16079]: warning: 61.141.72.43: hostname 43.72.141.61.broad.sz.gd.dynamic.163data.com.cn verification failed: Name or service not known
Jul 10 10:09:23 srv24-s-st postfix/smtpd[16079]: connect from unknown[61.141.72.43]
Jul 10 10:09:24 srv24-s-st postfix/smtpd[10344]: warning: unknown[183.7.120.155]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:24 srv24-s-st postfix/smtpd[16080]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:24 srv24-s-st postfix/smtpd[16080]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:24 srv24-s-st postfix/smtpd[16080]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:25 srv24-s-st postfix/smtpd[10344]: lost connection after AUTH from unknown[183.7.120.155]
Jul 10 10:09:25 srv24-s-st postfix/smtpd[10344]: disconnect from unknown[183.7.120.155]
Jul 10 10:09:25 srv24-s-st postfix/smtpd[10285]: connect from unknown[178.209.107.114]
Jul 10 10:09:25 srv24-s-st postfix/smtpd[10285]: 5F4A4DF04FA: client=unknown[178.209.107.114], sasl_method=CRAM-MD5, sasl_username=roman@skgsk.ru
Jul 10 10:09:25 srv24-s-st postfix/cleanup[6537]: 5F4A4DF04FA: message-id=<921240155.20120710100852@skgsk.ru>
Jul 10 10:09:25 srv24-s-st postfix/smtpd[14197]: connect from unknown[183.7.120.155]
Jul 10 10:09:26 srv24-s-st postfix/smtpd[4703]: lost connection after DATA from broadband-77-37-236-62.nationalcablenetworks.ru[77.37.236.62]
Jul 10 10:09:26 srv24-s-st postfix/smtpd[4703]: disconnect from broadband-77-37-236-62.nationalcablenetworks.ru[77.37.236.62]
Jul 10 10:09:26 srv24-s-st postfix/cleanup[28750]: 58189DF04EF: message-id=<20120710060923.58189DF04EF@smtp.jino.ru>
Jul 10 10:09:26 srv24-s-st postfix/smtpd[16077]: warning: 178.140.204.161: hostname broadband-178-140-204-161.nationalcablenetworks.ru verification failed: Name or service not known
Jul 10 10:09:26 srv24-s-st postfix/smtpd[16077]: connect from unknown[178.140.204.161]
Jul 10 10:09:26 srv24-s-st postfix/smtpd[4703]: warning: 81.177.6.31: address not listed for hostname srv24-s-st.jino.ru
Jul 10 10:09:26 srv24-s-st postfix/smtpd[4703]: connect from unknown[81.177.6.31]
Jul 10 10:09:26 srv24-s-st postfix/smtpd[4703]: disconnect from unknown[81.177.6.31]
Jul 10 10:09:27 srv24-s-st postfix/smtpd[10344]: warning: 81.177.6.31: address not listed for hostname srv24-s-st.jino.ru
Jul 10 10:09:27 srv24-s-st postfix/smtpd[10344]: connect from unknown[81.177.6.31]
Jul 10 10:09:27 srv24-s-st postfix/smtpd[10344]: disconnect from unknown[81.177.6.31]
Jul 10 10:09:27 srv24-s-st postfix/smtpd[27067]: warning: 109.126.10.42: hostname 109-126-10-42.eth.vladlink.net verification failed: Name or service not known
Jul 10 10:09:27 srv24-s-st postfix/smtpd[27067]: connect from unknown[109.126.10.42]
Jul 10 10:09:28 srv24-s-st postfix/smtpd[16079]: warning: unknown[61.141.72.43]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:28 srv24-s-st postfix/smtpd[16077]: warning: unknown[178.140.204.161]: SASL LOGIN authentication failed: UGFzc3dvcmQ6
Jul 10 10:09:28 srv24-s-st postfix/smtpd[16077]: lost connection after AUTH from unknown[178.140.204.161]
Jul 10 10:09:28 srv24-s-st postfix/smtpd[16077]: disconnect from unknown[178.140.204.161]
Jul 10 10:09:28 srv24-s-st postfix/smtpd[27067]: 64C08DF04EF: client=unknown[109.126.10.42], sasl_method=PLAIN, sasl_username=t.ivanova@dalvl.ru
Jul 10 10:09:28 srv24-s-st postfix/smtpd[16079]: lost connection after AUTH from unknown[61.141.72.43]
"""
	tmp_name = str(uuid.uuid1())
	f = open('/tmp/%s' % tmp_name, 'w')
	f.write(test_log)
	f.close()
	return tmp_name

def test_analyser(test_file):
	analyser = LogAnalyser(test_file)
	print ("total sended: %d " % analyser.total_sended())
	print ("total failed: %d " % analyser.total_failed())
	print ("Example sended by email [katya@dalvl.ru] -- %d " \
			% analyser.sended_by_email('katya@dalvl.ru'))
	
