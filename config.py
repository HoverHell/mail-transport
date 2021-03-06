# This file contains the default settings for various options.
# Please edit config.xml instead of this file

configFiles = ['config.xml', '/etc/pymailt.conf.xml']
configFile = None

jid = "mail"
host = ""
discoName = "Mail Transport"
pid = ""

mainServer = "127.0.0.1"
mainServerJID = "jabber.localhost"
port = "5347"
secret = "secret"

useComponentBinding = False
useRouteWrap = False
saslUsername = ""

debugFile = ""

dumpProtocol = False

smtpServer = "127.0.0.1"
watchDir = "~/Maildir/new/"

domains = []
fallbackToJid = ''

# 'plaintext' or 'html2text' or 'html'
preferredFormat = 'plaintext'
