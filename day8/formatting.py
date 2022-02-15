from asyncio.base_subprocess import WriteSubprocessPipeProto
from unicodedata import name

def my_print(txt):
       print(txt)

msg_template = """Hello {name},
       Thank you for joininig {website}. We are very 
       happy to have you with us.
       """ #.format(name="Arturo", website='cfe.sh')

def format_msg(my_name="Arturo", my_website="cfe.sh"):
       my_msg = msg_template.format(name=my_name, website=my_website)
       # my_msg.format(name=my_name, website=my_website) 
       # print(my_msg)
       return my_msg