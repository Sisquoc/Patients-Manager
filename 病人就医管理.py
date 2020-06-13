import random
import copy
class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None  # 初始设置下一节点为空


# 下面创建单链表，并实现其应有的功能
class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem,end="\n")
            cur = cur.next

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        return item

    def getfirst(self):
        '''获取链表首个元素'''
        cur = self.__head
        return cur.elem
    
    def find(self,item):
        '''查找某个元素'''
        cur = self.__head
        while cur != None:
            while cur.elem == item:
                return 1
                break
            cur = cur.next
            return 0

#挂号函数
def register(plink):#plink是挂号链表
    department = input("输入病人的科室:")
    number=str(random.randint(0, 9999))#生成一个0~9999的随机数作为病人编号
    pnumber=department+number#就诊号，包含科室和编号
    plink.append(pnumber)#将就诊号添加到挂号链表中
    print("病人的就诊号为：{}".format(pnumber))

#排队函数
def wait(plink,patientlink):#patientlink为排队链表
    pnumber=input("输入病人的就诊号:")
    if plink.find(pnumber):
        plink.remove(pnumber)
        patientlink.append(pnumber)
        print("病人{}已排队。".format(pnumber))
    elif patientlink.find(pnumber):
        print("病人{}已在排队中。".format(pnumber))
    else:
        print("病人{}不存在。".format(pnumber))

#就诊函数
def visit(patientq):
    if patientq.length()==0:#当排队队列中没人返回错误信息
        print("当前没有病人排队！")
    else:#否则将就诊号从排队队列中删除
        print("病人{}已就诊。".format(patientq.getfirst()))
        patientq.remove(patientq.getfirst())

#检查链表函数
def check(patientq):
    if patientq.length()==0:
        print("当前队列中没有病人。")
    else:
        patientq.travel()

#菜单函数
def menu():
    print("⑴挂号------预检，分科室，生成就诊号。")
    print("⑵排队------输入病人的就诊号，加入到病人排队队列中。")
    print("⑶就诊-------病人排队队列中最前面的病人就诊，并将其从队列中删除。")
    print("⑷查看排队------从队首到队尾列出所有的排队病人的病历号。")
    print("⑸下班---------退出运行。")

#文件写入函数
def wtext(name):
    path="./"+name+".txt"
    file = open(path,'w+',encoding="UTF-8")
    return file

#文件读取函数
def rtext(name):
    path="./"+name+".txt"
    file = open(path,'r+',encoding="UTF-8")
    return file


#主函数
def main():
    fregister=rtext("挂号病人管理")#读取挂号病人函数
    fqueue=rtext("排队病人管理")#读取排队病人函数
    plist=fregister.read().splitlines()#挂号病人列表
    qlist=fqueue.read().splitlines()#排队病人列表

    plink=SingleLinkList()
    patientlink=SingleLinkList()

    for i in plist:
        plink.append(i)
    for j in qlist:
        patientlink.append(j)

    choice=0#选择数
    menu()
    while(choice!=5):#选择
        choice=input("请输入你的选择：")
        if choice==str(1):
            register(plink)
        elif choice==str(2):
            wait(plink,patientlink)
        elif choice==str(3):
            visit(patientlink)
        elif choice==str(4):
            check(patientlink)
        elif choice==str(5):#退出系统并将挂号病人和排队病人保存到文件中
            fregister=wtext("挂号病人管理")
            fqueue=wtext("排队病人管理")
            cp_plink=copy.deepcopy(plink)
            cp_patientlink=copy.deepcopy(patientlink)
            for i in range(cp_plink.length()):
                fregister.write(cp_plink.getfirst()+"\n")
                cp_plink.remove(cp_plink.getfirst())
            for i in range(cp_patientlink.length()):
                fqueue.write(cp_patientlink.getfirst()+"\n")
                cp_patientlink.remove(cp_patientlink.getfirst())
            break
        else:
            print("请输入正确的代码！")
            continue
    print("已退出系统!")#退出信息
    
if __name__ == '__main__':
  main()
