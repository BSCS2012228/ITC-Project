from tkinter import*
import random
import time
import datetime
import smtplib
from email.message import EmailMessage

root=Tk()
root.geometry("1600x8000")
root.title("ITC Project By ITC Developers  (Shan Virani, Hamza, Razi, Rithick) ")
root.configure(bg='Black')

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
Tops.configure(bg='Black')

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f1.configure(bg='black')

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Times New Roman',50,'bold','italic','underline'),text="Restaurant Menu (Billing System) ",fg="SlateGray",bg="black",bd=14,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('Times New Roman',20,'bold'),text=localtime,fg='white',bg='black',bd=20,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('Times New Roman',30,'bold','italic'),text="Enter Quantity Below for Each Food Item you want : ",fg="White",bg="black",bd=14,anchor='w')
lblInfo.grid(row=3,column=0)


def Ref():
    if (Biryani.get()==""):
        CoBiryani=0
    else:
        CoBiryani=float(Biryani.get())


    
    if (Chicken_Roll.get()==""):
        CoChicken_Roll=0
    else:
        CoChicken_Roll=float(Chicken_Roll.get())



    if (Zinger_Burger.get()==""):
        CoZinger_Burger=0
    else:
        CoZinger_Burger=float(Zinger_Burger.get())



    if (ChickenBurger.get()==""):
        CoChickenBurger=0
    else:
        CoChickenBurger=float(ChickenBurger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())



                   
    CostofBiryani =CoBiryani * 200
    CostofDrinks=CoD * 50
    CostofChicken_Roll = CoChicken_Roll* 100
    CostofZinger_Burger = CoZinger_Burger * 150
    CostChickenBurger = CoChickenBurger* 100
    CostSandwich=CoSandwich * 150

    CostofMeal= "Rs", str('%.2f' % (CostofBiryani+CostofDrinks+CostofChicken_Roll+CostofZinger_Burger+CostChickenBurger+CostSandwich))

    PayTax=((CostofBiryani+CostofDrinks+CostofChicken_Roll+CostofZinger_Burger+CostChickenBurger+CostSandwich) * 0.17)

    TotalCost=(CostofBiryani+CostofDrinks+CostofChicken_Roll+CostofZinger_Burger+CostChickenBurger+CostSandwich)


    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Biryani.set("")
    Chicken_Roll.set("")
    Zinger_Burger.set("")
    SubTotal.set("")
    Total.set("")
    CoEmail.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    ChickenBurger.set("")
    Sandwich.set("")

def qOrder():
    Name = rand.get()
    Bir=Biryani.get()
    Roll = Chicken_Roll.get()
    Zing = Zinger_Burger.get()
    Burg = ChickenBurger.get()
    Dr = Drinks.get()
    Sand = Sandwich.get()
    ST = Tax.get()
    EmailTotal=Total.get()
    Email =CoEmail.get()
    msg = EmailMessage()
    msg['Subject'] = 'Your Order Has Been Placed'
    msg['From'] = 'itcdevelopers4321@gmail.com'
    msg['To'] = Email

    msg.add_alternative(f"""
    <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:purple;">The Restaurant by ITC Developers</h1>
                <h2 style="color:SlateGray;">You Have ordered From our Restaurant</h2>
                <h3 style="color:Black;">Hi {Name} ,Your order Has Been Placed </h1>
                <p>Your Order includes :</p>
                 <p>{Bir} = Biryani</p>
                 <p>{Roll} = Chicken Roll</p>
                 <p>{Zing} = Zinger Burger</p>
                 <p>{Burg} = Chicken Burger</p>
                 <p>{Sand} = Sandwhich</p>
                 <p>{Dr} = Drinks</p>
                <p>Your Sales Tax is : {ST}</p>
                <p>Your Total Cost is : {EmailTotal}</p>
                <h2 style="color:Green;">Thanks For Ordering</h2>
            </body>
        </html>
    """, subtype = 'html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('itcdevelopers4321@gmail.com','shan virani12')
        smtp.send_message(msg)

    
#====================================Defining a Variable===========================================================
rand = StringVar()
Biryani=StringVar()
Chicken_Roll=StringVar()
Zinger_Burger=StringVar()
SubTotal=StringVar()
Total=StringVar()
CoEmail=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
ChickenBurger=StringVar()
Sandwich=StringVar()


#====================================Restaraunt Info Column 1===========================================================

lblName= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Name of the Buyer",bd=16,anchor="w")
lblName.grid(row=0, column=0)
txtName=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtName.grid(row=0,column=1)

lblBiryani= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Biryani (Rs 200)",bd=16,anchor="w")
lblBiryani.grid(row=1, column=0)
txtBiryani=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Biryani,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtBiryani.grid(row=1,column=1)


lblChicken_Roll= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Chicken Roll (Rs 100)",bd=16,anchor="w")
lblChicken_Roll.grid(row=2, column=0)
txtChicken_Roll=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Chicken_Roll,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtChicken_Roll.grid(row=2,column=1)


lblZinger_Burger= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Zinger Burger (Rs 150)",bd=16,anchor="w")
lblZinger_Burger.grid(row=3, column=0)
txtZinger_Burger=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Zinger_Burger,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtZinger_Burger.grid(row=3,column=1)

lblChickenBurger= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Chicken Burger (Rs 100)",bd=16,anchor="w")
lblChickenBurger.grid(row=4, column=0)
txtChickenBurger=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=ChickenBurger,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtChickenBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Sandwich (Rs 150)",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtSandwich.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO Column 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Drinks (Rs 50)",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtDrinks.grid(row=0,column=3)

lblEmail= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Email",bd=16,anchor="w")
lblEmail.grid(row=1, column=2)
txtEmail=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=CoEmail,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtEmail.grid(row=1,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=2, column=2)
txtCost=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtCost.grid(row=2,column=3)

lblStateTax= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Sales Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),fg="White",bg="Black",text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1,fg='White', font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="SlateGray",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="white",font=('arial',16,'bold'),width=10,text="Total",bg="Green",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="white",font=('arial',16,'bold'),width=10,text="Reset",bg="blue",command=Reset).grid(row=7,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="White",font=('arial',16,'bold'),width=10,text="Exit",bg="Red",command=qExit).grid(row=7,column=2)

btnOrder=Button(f1,padx=16,pady=8,bd=16,fg="White",font=('arial',16,'bold'),width=10,text="Order/Email",bg="SlateGray",command=qOrder).grid(row=7,column=3)

root.mainloop()


