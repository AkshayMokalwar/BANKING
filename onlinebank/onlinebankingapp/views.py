from django.shortcuts import render,redirect
from django.contrib import messages 
from django.http import HttpResponse , HttpResponseRedirect
import sqlite3
connection=sqlite3.connect('dbonlinebanking.sql')
c=connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS tblregistration(RedID INTEGER PRIMARY KEY AUTOINCREMENT ,Firstname TEXT , Lastname TEXT , username TEXT , Password TEXT , EmailID TEXT,Account No TEXT ,Balance Real ,Address TEXT )')
# Create your views here.
def login_view(request):
	if request.method=='POST':
		username=request.POST['txtusername']
		password=request.POST['txtpassword']
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT RedID ,Account No,Balance from tblregistration WHERE username="%s" AND Password="%s" ' %(username,password))
		records=c.fetchall()
		if records is not None :
			for a, b, c in records:
				request.session['RedID']=a
				request.session['Account No']=b
				request.session['Balance']=c
				return render(request,'onlinebankingapp/Home.html')
		else :
			return render(request,'onlinebankingapp/dummy1.html')
		connection.commit()
		connection.close()
		return redirect('/dummy1/')

	elif request.method=='GET':
		return render(request,'onlinebankingapp/login.html')

def dummy1_view(request):
	return render(request,'onlinebankingapp/dummy1.html')


def registration_view(request):
	if request.method=='POST':
		firstname=request.POST['txtfirstname']
		lastname=request.POST['txtlastname']
		username=request.POST['txtusername']
		password=request.POST['txtpassword']
		emailid=request.POST['txtemailid']
		accountno=request.POST['txtaccountno']
		balance=request.POST['txtbalance']
		address=request.POST['txtaddress']
		mobileno=request.POST['txtmobileno']

		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('INSERT INTO tblregistration values(Null,?,?,?,?,?,?,?,?)',(firstname,lastname,username,password,emailid,accountno,balance,address))
		connection.commit()
		connection.close()
		return render(request,'onlinebankingapp/display.html')
	elif request.method=='GET':
		return render(request,'onlinebankingapp/registration.html')

def change_view(request):
	if(request.method=="GET"):
		return render(request,'onlinebankingapp/ChangePassword.html')
	elif(request.method=="POST"):
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		oldpassword=request.POST['txtold']
		newpassword=request.POST['txtnew']
		confirmpassword=request.POST['txtconfirm']

		c.execute("SELECT RegID ,EmailID from tblregistration WHERE Password=? ",(oldpassword,))
		allrecords=c.fetchall()
		if allrecords is not None:
			for a,b in allrecords:
				if newpassword==confirmpassword:
					c.execute('''UPDATE tblregistration SET Password =? WHERE  RegID =? ''' ,(newpassword,a))
					connection.commit()
					connection.close()
					return render(request,'onlinebankingapp/Login.html')
				else:
					return render(request,'onlinebankingapp/dummy1.html')
		else:
			return render(request,'onlinebankingapp/dummy.html')

	return render(request,'onlinebankingapp/ChangePassword.html')


def forget_view(request):
	if(request.method=="GET"):
		return render(request,'onlinebankingapp/forgetpassword.html')
	elif(request.method=="POST"):
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		EmailID=request.POST['txtemailid']
		connection=sqlite3.connect('dbonlinebanking.sql')
		c.execute('SELECT RedID,Password from tblregistration WHERE EmailID=?',(EmailID))

		allrecords=c.fetchall()
		return render(request,'onlinebankingapp/dummy.html',{'Records':allrecords})

		connection.close()
	return render(request,'onlinebankingapp/forgetpassword.html')

def deposit_view(request):
	if(request.method=="GET"):
		RedID=request.session['RedID']
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT Account No ,Balance from tblregistration WHERE RedID=?',(RedID,))
		allrecords=c.fetchall()
		return render(request,'onlinebankingapp/Deposit.html',{'Students':allrecords})
	elif request.method=="POST":
		RedID=request.session['RedID']
		balance=request.POST['txtbalance']
		deposit=request.POST['txtdeposit']
		if(balance and deposit is not None ):
			total=float(balance)+float(deposit)

			connection=sqlite3.connect('dbonlinebanking.sql')
			c=connection.cursor()
			c.execute('''UPDATE tblregistration SET Balance =? WHERE RedID=?''',(total,RedID))
			
			connection.commit()
			connection.close()
			return redirect('/balance/')
		else:
			return render(request,'onlinebankingapp/dummy1.html')


def withdraw_view(request):
	if(request.method=="GET"):
		RedID=request.session['RedID']
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT Account No , Balance from tblregistration WHERE RedID=?',(RedID,))
		allrecords=c.fetchall()

		return render(request,'onlinebankingapp/withdraw.html',{'Students':allrecords})
	elif request.method=="POST":
		RedID=request.session['RedID']
		balance=request.POST['txtbalance']
		withdraw=request.POST['txtwithdraw']
		if(balance and withdraw is not None ):
			total=float(balance)-float(withdraw)

			connection=sqlite3.connect('dbonlinebanking.sql')
			c=connection.cursor()
			c.execute('''UPDATE tblregistration SET Balance =? WHERE RedID=?''',(total,RedID))
			
			connection.commit()
			connection.close()
			return redirect('/balance/')
		else:
			return render(request,'onlinebankingapp/dummy1.html')

def balance_view(request):
	RedID=request.session['RedID']
	connection=sqlite3.connect('dbonlinebanking.sql')
	c=connection.cursor()
	c.execute('SELECT Firstname,Account No ,Balance from tblregistration WHERE RedID=?',(RedID,))
	allrecords=c.fetchall()
	return render(request,'onlinebankingapp/Balance.html',{'Records':allrecords})

def home_view(request):
	return render(request,'onlinebankingapp/Home.html')

def display_view(request):
	if request.method=="GET":
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT Firstname ,Lastname,Username,Password, EmailID, Account No , Balance,Address from tblregistration')
		allrecords=c.fetchall()
		return render(request,'onlinebankingapp/display.html',{'Students':allrecords})


def bind_firstname(request):
	if request.method=='GET':
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT RedID , Firstname from tblregistration ')
		allrecords=c.fetchall()
		return render(request,'onlinebankingapp/bind.html',{'Students':allrecords})

# Create your views here.
def getid_firstname(request):
	if request.method=='GET':
		regID=request.GET.get('Regid')
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT Lastname from tblregistration WHERE RedID=?',(regID,))
		data=c.fetchall()
		if( data is  None):
			return render(request,'onlinebankingapp/dummy1.html')
		else:
			return render(request,{"data":data},status=200)
		