from cProfile import label
from genericpath import exists
from logging import raiseExceptions
from operator import contains
from sre_constants import BIGCHARSET
from tkinter import*
from tokenize import String
from datetime import date
from tkinter import messagebox
import json
from functools import partial
import os



class Bill_App:
    


    def __init__(self,root):

        self.root=root
        self.root.geometry("1300x700+0+0")     #width*height+startX+StartY
        self.root.title("Billing Software")
        bg_color="lightblue"
        #self.root.state("zoomed")
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="lightgrey",fg="darkblue",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

#-----------------Variables Initialization--------------

        # self. ---> instance variables
        
        self.new_cat=StringVar()

  

        # customer--------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        
        
        self.item_name=StringVar()
        self.item_num = StringVar()
        #adding item to category..selected category
        self.clkk = StringVar()
        self.new_item_name=StringVar()
        self.item_number=IntVar()
        self.sel_unit=StringVar()
        self.price=IntVar()

        self.clk_cat_upd=StringVar()
        self.clk_item_upd=StringVar()

        self.item_Opt1=["Items"]
        self.cat_Opt1=[]

        self.checkk=0

        self.upd_item_no=IntVar()
        self.upd_price=IntVar()

        self.clicked = StringVar()
        self.opts=[""]
        self.clicked.set( "Select Item" )

        self.detail_chekk=0

        self.totl=IntVar()
        self.totl=0

        #---------Getting bill Number----------
        loc="Bills/bill_info.json"
        with open(loc,"r") as bno:
            b_no=json.load(bno)
            b_no_keys=list(b_no.keys())
            last_bill_no=b_no_keys[-1]
            self.bill_no.set(str(int(last_bill_no)+1))
            bno.close()
        
        #---------Customer Frame----------
        F1=LabelFrame(self.root,text="New Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="darkblue",bg=bg_color)
        F1.place(x=0,y=80,width=800)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="brown",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=8,pady=10)
        cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=8)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="brown",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10)
        cphn_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_phone,bd=7,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="brown",font=("times new roman",18,"bold")).grid(row=1,column=3,padx=10,pady=10)
        c_bill_txt=Label(F1,width=10,font="arial 15 bold ",fg="lightgreen",bd=7,textvariable=self.bill_no,relief=SOLID).grid(row=1,column=4,pady=5,padx=10,sticky="W")

        date_lbl=Label(F1,text=date.today(),bg="lightblue",fg="blue",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=10,pady=10)

        detail_btn=Button(F1,text="Add\nDetail",width=10,bd=4,font="arial 10 bold ",bg="gold",fg="blue",command=self.welcome_bill).grid(row=1,column=2,padx=12,pady=4,sticky="E")

       # Existing Customer Details-------
        
        fnc=LabelFrame(self.root,text="Existing Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="darkblue",bg=bg_color)
        fnc.place(x=810,y=80,width=550,height=120)

        Existph=Label(fnc,text="Phone No.",bg=bg_color,fg="brown",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10)
        Ex_Ph=Entry(fnc,width=15,font="arial 15",textvariable=self.c_phone,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        detail_btn=Button(fnc,text="Add\nDetail",width=10,bd=4,font="arial 10 bold ",bg="blue",fg="white").grid(row=0,column=2,padx=12,pady=4,sticky="E")



       # Bill Menu----------------

        self.F2=LabelFrame(self.root,text="Bill Menu",bd=10,relief=RAISED,font=("times new roman",15,"bold"),fg="darkblue",bg="#aed581")
        self.F2.place(x=0,y=230,width=800,height=320)

        
       


        #--------category dropdown------------------
        with open('category.json', 'r') as f:
            a = json.load(f)
        kk=a.keys()
        self.Opts1=[]
        for k in kk:
            self.Opts1.append(a[k])
        f.close()
        
        self.clk = StringVar()
        self.clk.set("Select Category")

       
        category=Label(self.F2,text="Category : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=0,pady=10)
        self.cat_items=OptionMenu(self.F2 , self.clk , *self.Opts1, command=self.sel_catu ).grid(row=1,column=0,padx=4,pady=20)
        
        
        
        
        
        item=Label(self.F2,text="Item Name :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=1,padx=4,pady=4,sticky="w")
        #item__name=Entry(F2,width=10,font=("times new roman",16,"bold"),textvariable=self.item_name,relief=SUNKEN).grid(row=0,column=1,padx=4,pady=4)
        self.drop=OptionMenu(self.F2 , self.clicked , *self.opts ).grid(row=1,column=1,padx=4,pady=4)

        

        itemnum=Label(self.F2,text="No. of Items :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=2,padx=4,pady=4,sticky="w")
        item__num=Entry(self.F2,width=10,font=("times new roman",16,"bold"),textvariable=self.item_num,relief=SUNKEN).grid(row=1,column=2,padx=4,pady=4)

       

        add_btn=Button(self.F2,text="Add",width=6,bd=3,font="arial 16 bold",fg="lightblue",command=self.add_bill).grid(row=1,column=3,padx=10,pady=10)


        gen_btn=Button(self.F2,text="Generate Bill",width=10,bd=7,font="arial 12 bold",bg="blue",command=self.gen_bill).grid(row=2,column=2,padx=4,pady=30,sticky="S")
        clear_btn=Button(self.F2,text="Clear",width=8,bd=7,font="arial 12 bold",bg="#ef6c00",command=self.clrr).grid(row=2,column=3,padx=12,pady=30,sticky="S")
        exit_btn=Button(self.F2,text="Exit",width=8,bd=7,font="arial 12 bold",bg="red",command=self.exxt).grid(row=2,column=4,padx=4,pady=30,sticky="W")



       
       #---------Bill Area

        F3=LabelFrame(self.root,bd=10,relief=GROOVE)
        F3.place(x=801,y=200,width=550,height=500)
        bill_title=Label(F3,text="Bill",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F3,orient=VERTICAL)
        self.txtarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        

        #-------Inventory---------

        F4=LabelFrame(self.root,text="Check Inventory",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="darkblue",bg=bg_color)
        F4.place(x=0,y=560,height=140,width=400)

        inv_btn=Button(F4,text="Inventory",command=self.inv,width=6,bd=3,font="arial 16 bold",fg="lightblue").grid(row=0,column=0,padx=70,pady=30)
        
        #--------------Bill History-----------

        F5=LabelFrame(self.root,text="Bill History",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="darkblue",bg=bg_color)
        F5.place(x=410,y=560,height=140,width=390)

        bill_his=Button(F5,text="Bills",command=self.bill_his,width=6,bd=3,font="arial 16 bold",fg="lightblue").grid(row=0,column=0,padx=70,pady=30)

       
        #self.welcome_bill()
    def clrr(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.txtarea.delete("1.0",END)
        self.totl=0
        self.item_num.set("")
        self.detail_chekk=0

    def exxt(self):
        exit()



    def bill_his(self):
        b_his = Toplevel(root)

        b_his.title("Inventory")
        title = Label(b_his,text="Bill History",bd=12,relief=GROOVE,bg="lightgrey",fg="darkred",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        b_his.state("normal")
     # sets the geometry of toplevel
        b_his.geometry("1380x700")

    #---------frame to show bills---------
        F_bill=LabelFrame(b_his,bd=10,bg="#2E3033",fg="white")
        F_bill.place(x=0,y=80,width=630,height=620)
        bills_title=Label(F_bill,text="Bills",font="arial 10 bold",bd=7,relief=GROOVE,fg="lightblue").pack(fill=X)
        scrl_y=Scrollbar(F_bill,orient=VERTICAL)
        bill_txtarea=Text(F_bill,yscrollcommand=scrl_y.set,bg="#2E3033")
        scrl_y.pack(side=RIGHT,fill=Y)
        scrl_y.config(command=bill_txtarea.yview)
        bill_txtarea.pack(fill=BOTH,expand=1)

        bill_txtarea.insert(END,f"\n Bill Number\t\tName\t\tDate\n\n")
        with open("Bills/bill_info.json","r") as bi:
            binfo=json.load(bi)
            kk=binfo.keys()
            for key in kk:
                bill_txtarea.insert(END,f"\n {key}\t\t{binfo[key][0]}\t\t{binfo[key][1]}")
            bi.close()


        #----------frame to take bill number--------
        F_info=LabelFrame(b_his,text="Check any previous bill",bd=10,relief=RAISED,font=("times new roman",15,"bold"),fg="darkred",bg="#aed581")
        F_info.place(x=640,y=80,width=710,height=150)

        self.ent_bill_no=StringVar()

        ent_bill=Label(F_info,text="Enter Bill Number",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=0,padx=4,pady=4,sticky="e")

        bil__num=Entry(F_info,width=18,font=("times new roman",16,"bold"),textvariable=self.ent_bill_no,relief=SUNKEN).grid(row=1,column=0,padx=4,pady=4)
        

        srch=Button(F_info,text="Search",width=6,bd=3,font="arial 16 bold",fg="lightblue",command=self.showbill).grid(row=1,column=3,padx=10,pady=10)

        





        self.sh_bill=LabelFrame(b_his,bd=10,bg="#2E3033",fg="white")
        self.sh_bill.place(x=640,y=230,width=710,height=460)
        bills_title=Label(self.sh_bill,text="Bill Number {}",font="arial 10 bold",bd=7,relief=GROOVE,fg="lightblue").pack(fill=X)
        scrl_y=Scrollbar(self.sh_bill,orient=VERTICAL)
        self.sh_bill_txtarea=Text(self.sh_bill,yscrollcommand=scrl_y.set,bg="#2E3033")
        scrl_y.pack(side=RIGHT,fill=Y)
        scrl_y.config(command=self.sh_bill_txtarea.yview)
        self.sh_bill_txtarea.pack(fill=BOTH,expand=1)

        
        


    def showbill(self):
        try:
            
            bbno=self.ent_bill_no.get()
            if bbno =="":
                raise Exception("emtpy field")
       
            with open("Bills/bill_info.json","r") as bs:
                b_show=json.load(bs)
                cust_name=b_show[str(bbno)][0]
                bs.close()
            f_open=str(bbno)+str(cust_name)+".txt"

            self.sh_bill_txtarea.delete("1.0",END)
            file_open="Bills/{}".format(f_open)
            ftp=open(file_open,"r")
            data=ftp.read()
            self.sh_bill_txtarea.insert(END, data)
            ftp.close()
        except:
            messagebox.showerror("Error","Invalid Bill Number")



    
    def add_bill(self):
        try:
            if self.detail_chekk==0:
                raise Exception("Details Not Entered")
            self.detail_chekk=2
            cat=self.clk.get()
            cate=cat+".json"
            it=self.clicked.get()
            qt=self.item_num.get()

            #pr=80
            with open(cate,'r+') as cat:
                    a = json.load(cat)
                    pr=a[it][2]
                    itss=int(a[it][1])
                    if itss==0 or itss<int(qt):
                        raise Exception("NO. of Items Exceeds")
                    a[it][1]=int(a[it][1]) - int(qt)
                    cat.seek(0)
                    json.dump(a, cat, indent = 4)
                    cat.close()
            
                
            tot=int(qt)*int(pr)
            self.totl=self.totl+tot
            self.txtarea.insert(END,f"\n {it}\t\t{qt}\t\t{pr}\t\t{tot}")
        except Exception as e:
            messagebox.showerror("Error",str(e))



    def welcome_bill(self):
        try:
            if self.c_name.get() == "" or self.c_phone.get()=="":
                raise Exception("Required Field Empty")
            if self.detail_chekk==1:
                raise Exception("Details Already added")
            self.detail_chekk=1
            #self.txtarea.delete("1.0",END)
            self.txtarea.insert(END,"\t\t Retail Business Bill")
            self.txtarea.insert(END,f"\n\n Bill Number : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n Date : {date.today()}")
            self.txtarea.insert(END,f"\n\n============================================================")

            self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice\t\tTotal")


            self.txtarea.insert(END,f"\n============================================================")
        except:
            messagebox.showerror("Error","Field Cannot be Empty")
    
    def gen_bill(self):
        try:
            if self.detail_chekk != 2:
                raise Exception("no item added")
            self.txtarea.insert(END,f"\n----------------------------------------------------------")
            self.txtarea.insert(END,f"\n Grand Total\t\t\t\t\t\t{self.totl}")

            
            bil_n=self.bill_no.get()
            cus_name=self.c_name.get()
            bill_name=str(bil_n)+str(cus_name)
            
            nam="Bills/{}.txt".format(bill_name)

            with open(nam,"w") as f:
                f.write(self.txtarea.get(1.0, END))
                f.close()

            #---------writing to bill no-------file------
            locc="Bills/bill_info.json"
            with open(locc,"r+") as bilno:
                 a=json.load(bilno)
                 a[bil_n]=[str(cus_name),str(date.today())]
                 bilno.seek(0)
                 json.dump(a, bilno, indent = 4)
                 bilno.close()

            #----printing bill-----
            #--only for windows----

            # act_path="C:/Users/abc/Desktop/Bill Management/"
            # file_path=act_path+nam
            # try:
            #     os.startfile(file_path,"print")
            # except:
            #     messagebox.showerror("error","printing error")

            #------clearing stuff----------
            self.bill_no.set(int(self.bill_no.get())+1)
            self.c_name.set("")
            self.c_phone.set("")
            messagebox.showinfo("Success","bill area will be cleared, Check bill history")
            self.txtarea.delete("1.0",END)


        except:
            messagebox.showerror("Error","No item Added")
    
    def sel_catu(self,a):
        #messagebox.showinfo("showinfo","Success")
        
        sel=self.clk.get()
        its=sel+".json"
        
        with open(its,'r') as items:
            it=json.load(items)
            
            options = it.keys()
           
            self.opts=options
        #self.drop.config( *self.opts = *opts3+self.opts )
        self.drop=OptionMenu(self.F2 , self.clicked , *self.opts ).grid(row=1,column=1,padx=4,pady=4)
        self.clicked.set( "Select Item" )

    def add_c(self,invt):

        try:
            nn=self.new_cat.get()

            if nn=="":
                raise Exception("Empty Field")
            name=str(nn+".json")
        
        
            if exists(name):
                raise Exception("Already exists") 
            f = open(name, "x")
            f.write("{ }")
            with open('category.json','r') as cat:
                a = json.load(cat)
            kk=list(a.keys())

            end=int(kk[-1])
            
            ind=end+1

            with open('category.json','r+') as cat_add:
                ff = json.load(cat_add)
                ff[ind]=nn
                cat_add.seek(0)
                json.dump(ff, cat_add, indent = 4)
                #cat_add.write(add_string)
            
            messagebox.showinfo("showinfo","Success")
            self.new_cat.set("")
            with open('category.json', 'r') as f:
                a = json.load(f)
                kk=a.keys()
                Opt1=[]
            for k in kk:
                Opt1.append(a[k])
            f.close()
            self.cat_Opt1=Opt1
            self.cat_items=OptionMenu(self.Finv1 , self.clkk , *Opt1 ).grid(row=0,column=1,padx=4,pady=20)
            self.cat_item=OptionMenu(self.Finv2 , self.clk_cat_upd , *self.cat_Opt1 ,command=partial(self.upd_lst,invt)).grid(row=0,column=1,padx=4,pady=20)
            self.cat_items=OptionMenu(self.F2 , self.clk , *Opt1, command=self.sel_catu ).grid(row=1,column=0,padx=4,pady=20)

            
        except Exception as e:
            
            messagebox.showerror("showerror", str(e))
            invt.destroy()
    
    def add_item(self):
        name=self.new_item_name.get()
        num=self.item_number.get()
        price=self.price.get()
        unit=self.sel_unit.get()
        cat=self.clkk.get()

        file=str(cat)+".json"
        try:
            if name and num and price and unit is not NONE:
                # with open(file,'r') as fi:
                #     fi=json.load(fi)
                # ks=fi.keys()
                with open(file,'r+') as f:
                    ff=json.load(f)
                    ks=list(ff.keys())
                    if name in ks:
                        raise Exception(" already exists")
                        
                    ff[name]=[unit,num,price]
                    f.seek(0)
                    json.dump(ff, f, indent = 4)
                messagebox.showinfo("showinfo","Success")
        except:
              messagebox.showinfo("showinfo","Something went wrong")
    


    def upd_lst(self,invt,*args):
        self.checkk=self.checkk+1
        cat=self.clk_cat_upd.get()
        cat_file=cat+".json"

        #messagebox.showinfo("error",cat_file)
        with open(cat_file, 'r') as f:
            a = json.load(f)
        kk=a.keys()
        
        self.item_Opt1=[]
        for k in kk:
            self.item_Opt1.append(k)

        self.item_sel=OptionMenu(self.Finv2 , self.clk_item_upd , *self.item_Opt1 ).grid(row=1,column=1,padx=4,pady=20)

        # invt.destroy()
        # self.inv()

    def info_update(self):
        sel_cat=self.clk_cat_upd.get()
        cat=sel_cat+".json"
        ite=self.clk_item_upd.get()
        price=self.upd_price.get()
        no=self.upd_item_no.get()
        try:
            if sel_cat=="Select Category" or ite=="Select Item":
                 raise Exception("invalid")

            with open (cat,"r+") as f:
                ff=json.load(f)
                u=ff[ite][0]
                n=ff[ite][1]
                p=ff[ite][2]

                if(price==0):
                    ff[ite]=[u,n+no,p]
                else:
                    ff[ite]=[u,n+no,price]
                f.seek(0)
                json.dump(ff, f, indent = 4)
            messagebox.showinfo("Info","Update Successful")
            self.clk_cat_upd.set("Select Category")
            self.clk_item_upd.set("Select Item")
            self.upd_price.set(0)
            self.upd_item_no.set(0)
        except:
            messagebox.showerror("Error","Something Went Wrong")

    def show_detail(self,*args):

        #messagebox.showinfo("info","helllo")
        self.sharea.delete('1.0', END)
        self.sharea.insert(END,f"\n Items\t\tQTY\t\tsell Unit\t\tPrice\n")

        cc=self.clk_.get()
        categ=cc+".json"
        with open(categ, 'r') as f:
                a = json.load(f)
                kkeys=a.keys()
        for item in kkeys:
            self.sharea.insert(END,f"\n {item}\t\t{a[item][1]}\t\t{a[item][0]}\t\t{a[item][2]}")

                

    




    def inv(self):

      # Toplevel object which will
    # be treated as a new window
        
        invt = Toplevel(root)

        invt.title("Inventory")
        title = Label(invt,text="Inventory",bd=12,relief=GROOVE,bg="lightgrey",fg="darkred",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        invt.state("normal")
     # sets the geometry of toplevel
        invt.geometry("1380x700")

    #----------Frame for adding category------------
        Finv0=LabelFrame(invt,text="Add New Category",bd=10,relief=RAISED,font=("times new roman",15,"bold"),fg="darkred",bg="#aed581")
        Finv0.place(x=0,y=80,width=700,height=120)

        category=Label(Finv0,text="Category : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=0,pady=20)
        cat_new=Entry(Finv0,width=10,font=("times new roman",16,"bold"),relief=SUNKEN,textvariable=self.new_cat).grid(row=0,column=1,padx=4,pady=4,sticky='W')

        add_cat_btn=Button(Finv0,text="Add",width=6,bd=3,font="arial 16 bold",fg="darkblue",command=partial(self.add_c, invt)).grid(row=0,column=3,padx=60,pady=10)

    
  #--------Frame for Adding new item ---------#
        self.Finv1=LabelFrame(invt,text="Add New Item to Inventory",bd=10,relief=RAISED,font=("times new roman",15,"bold"),fg="darkred",bg="#aed581")
        self.Finv1.place(x=0,y=210,width=700,height=380)

        with open('category.json', 'r') as f:
            a = json.load(f)
        kk=a.keys()
        Opt1=[]
        for k in kk:
            Opt1.append(a[k])
        f.close()

        self.clkk.set("select item")

        
        cat_sel=Label(self.Finv1,text="Category : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=0,pady=20)
        self.cat_items=OptionMenu(self.Finv1 , self.clkk , *Opt1 ).grid(row=0,column=1,padx=4,pady=20)
    

        item=Label(self.Finv1,text="Item Name :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=1,column=0,padx=4,pady=4,sticky="w")
        item_new=Entry(self.Finv1,width=10,font=("times new roman",12,"bold"),relief=SUNKEN,textvariable=self.new_item_name).grid(row=1,column=1,padx=4,pady=4,sticky='W')

        itemnum=Label(self.Finv1,text="No. of Items :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=2,column=0,padx=4,pady=4,sticky="w")
        item__num=Entry(self.Finv1,width=10,font=("times new roman",12,"bold"),relief=SUNKEN,textvariable=self.item_number).grid(row=2,column=1,padx=4,pady=4)

        price=Label(self.Finv1,text="MRP per unit :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=3,column=0,padx=4,pady=4)
        item_price=Entry(self.Finv1,width=10,font=("times new roman",12,"bold"),relief=SUNKEN,textvariable=self.price).grid(row=3,column=1,padx=4,pady=4,sticky='W')

        Unit=Label(self.Finv1,text="unit : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=4,column=0,padx=4,pady=4)
        item_unit=Entry(self.Finv1,width=10,font=("times new roman",12,"bold"),relief=SUNKEN,textvariable=self.sel_unit).grid(row=4,column=1,padx=4,pady=4,sticky='W')

    

        add_btn=Button(self.Finv1,text="Add",width=6,bd=3,font="arial 16 bold",fg="darkblue",command=self.add_item).grid(row=2,column=3,padx=60,pady=10)

#--------Frame for Updation ---------#
        self.Finv2=LabelFrame(invt,text="Update Existing Inventory",bd=10,relief=RAISED,font=("times new roman",15,"bold"),fg="darkred",bg="#aed581")
        self.Finv2.place(x=710,y=80,width=630,height=400)

        with open('category.json', 'r') as f:
            a = json.load(f)
        kk=a.keys()
        self.cat_Opt1=[]
        for k in kk:
            self.cat_Opt1.append(a[k])
        f.close()


        if(self.checkk==0):
            self.clk_cat_upd.set("Category")
        

        
        cat_selec=Label(self.Finv2,text="Category : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=0,column=0,pady=20)
        self.cat_item=OptionMenu(self.Finv2 , self.clk_cat_upd , *self.cat_Opt1 ,command=partial(self.upd_lst,invt)).grid(row=0,column=1,padx=4,pady=20)



        self.clk_item_upd.set("Select Item")
        
    
        Item_sel=Label(self.Finv2,text="Item Name : ",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=1,column=0,pady=20)
        self.item_sel=OptionMenu(self.Finv2 , self.clk_item_upd , *self.item_Opt1 ).grid(row=1,column=1,padx=4,pady=20)

        itemnum=Label(self.Finv2,text="Add Items no. :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=2,column=0,padx=4,pady=4)
        item__num_update=Entry(self.Finv2,width=10,font=("times new roman",16,"bold"),relief=SUNKEN,textvariable=self.upd_item_no).grid(row=2,column=1,padx=4,pady=4)

        price=Label(self.Finv2,text="updated price :",font=("times new roman",20,"bold"),bg="#aed581",fg="#37474f").grid(row=3,column=0,padx=4,pady=4)
        item_price_update=Entry(self.Finv2,width=10,font=("times new roman",16,"bold"),relief=SUNKEN,textvariable=self.upd_price).grid(row=3,column=1,padx=4,pady=20)


        add_btn=Button(self.Finv2,text="Update",width=6,bd=3,font="arial 16 bold",fg="darkblue",command=self.info_update).grid(row=2,column=3,padx=60,pady=30)
    
        info=Label(self.Finv2,text="write 0(zero) for field ",font=("times new roman",16,"bold"),bg="#aed581",fg="red").grid(row=4,column=0,padx=4,pady=20)
        info2=Label(self.Finv2,text="not to update",font=("times new roman",16,"bold"),bg="#aed581",fg="red").grid(row=4,column=1,padx=4,pady=20)
    
    
    #--------Frame for Viewing---------#
        self.Finv3=LabelFrame(invt,text="View Category details",font=("times new roman",15,"bold"),fg="lightblue",bg="#2E3033")
        self.Finv3.place(x=0,y=600,width=700,height=100)

        self.clk_=StringVar()
        self.clk_.set("Select Category")

        sel_category=Label(self.Finv3,text="Category : ",font=("times new roman",18,"bold"),bg="#2E3033",fg="white").grid(row=0,column=1,pady=20)
        cat_it=OptionMenu(self.Finv3 , self.clk_ , *self.cat_Opt1,command=self.show_detail).grid(row=0,column=2,padx=4,pady=20)
        
        

        self.Finv4=LabelFrame(invt,bd=10,bg="#2E3033",fg="white")
        self.Finv4.place(x=710,y=485,width=630,height=200)
        sh_title=Label(self.Finv4,text="details of Category",font="arial 10 bold",bd=7,relief=GROOVE,fg="lightblue").pack(fill=X)
        scrl_y=Scrollbar(self.Finv4,orient=VERTICAL)
        self.sharea=Text(self.Finv4,yscrollcommand=scrl_y.set,bg="#2E3033")
        scrl_y.pack(side=RIGHT,fill=Y)
        scrl_y.config(command=self.txtarea.yview)
        self.sharea.pack(fill=BOTH,expand=1)

    



root=Tk()
obj=Bill_App(root)
root.mainloop()

