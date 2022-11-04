from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):    #view-function #url=welcome/
      print("welcome/ url is requested & display() is executed")
      ss="<center><h2 style='color:blue;'>Hello User, Welcome To Django First Project First-App</h2><hr color='red' width='80%' size='5'/></centre>" 
      return HttpResponse(ss)
      
def show(request):             #url=welcome2/
      ss='''<!-- 
    HTML web page to display welcome msg using diff. headings
 -->
 <html>	
    <head>
	   <title>***welcome-message***</title> 
       <style>
	   h1{color:blue;}
	   h2{color:orange;}
	   h3{color:deeppink;}
	   h4{color:green;}
	   h5{color:purple;}
	   h6{color:red;}
	   
	   h1,h3,h5{background-color:lightgreen;}
	   h2,h4,h6{background-color:lightblue;}		

	   </style>
    </head>
     <body> 
	     <center>
		  <h1>Welcome To DJANGO HTML Web Page</h1>
		  <hr color='black' width='95%'/>
          <h2>Welcome To DJANGO HTML Web Page</h2>
		  <hr color='black' width='85%'/>
		  <h3>Welcome To DJANGO HTML Web Page</h3>
		  <hr color='black' width='75%'/>
		  <h4>Welcome To DJANGO HTML Web Page</h4>
		  <hr color='black' width='65%'/>
		  <h5>Welcome To DJANGO HTML Web Page</h5>
		  <hr color='black' width='55%'/>
          <h6>Welcome To DJANGO HTML Web Page</h6>
		  <hr color='black' width='45%'/>
		 </center>
     </body>
 </html> 
''' 
      return HttpResponse(ss)

def hello(request):              #url=hello/
     print("hello/ url is requested & hello() is executed")   
     ss='''
      <html>
      <head>
      <title>welcome message</title> 
      <style>
          h1{color:red}
          h2{color:darkgreen}
          h3{color:darkorange}
          h1,h2,h3{background-color:pink;
                   width:60%;
                   border:2px solid brown;}
      </style>    
      </head>
      <body>
      <center>
          <hr color='blue' width='50% /'>
          <h1>hello user....!!</h1>
          <hr color='blue' width='50% /'>
          <h2>welcome to django..</h2>
          <hr color='blue' width='50% /'>
          <h3>have a nice day..</h3>
          <hr color='blue' width='50% /'>
      </center>    
      </body>
      
      </html>
          '''
     return HttpResponse(ss)     
        
import time        
def disdatetime(request):
      print("dtime/ url is requested & disdatetime() is executed")
      ct=time.ctime()
      print("client request date & time on server:",ct)
      ss='''
      <html>
      <head>
      <title>welcome message</title> 
      <style>
          h1{color:red}
          h2{color:darkgreen}
          h3{color:darkorange}
          h1,h2,h3{background-color:pink;
                   width:60%;
                   border:2px solid brown;}
      </style>    
      </head>
      <body>
      <center>
          <hr color='blue' width='50% /'>
          <h1>hello user....!!</h1>
          <hr color='blue' width='50% /'>
          <h2>server date & time</h2>
          <hr color='blue' width='50% /'>
          <h3>''',ct,'''</h3>
          <hr color='blue' width='50% /'>
      </center>    
      </body>
      
      </html>
      '''  
      return HttpResponse(ss)

#multiple urls for same view()
def demo(req):
    print("mulitple-Requests-URLs same respose");
    htmldata='''
       <center>
       <h1>hello demo user </h1><hr />
       <h2>this is same output for multiple req url</h2><hr />
       <h3>have a nice day</h3><hr />
       </center>
          '''     
    return HttpResponse(htmldata)

#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
    
     
     
     
     
     
     
     
     
     
     
           