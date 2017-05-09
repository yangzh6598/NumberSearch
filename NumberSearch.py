#Name:yang zhang
#sectin:A1
#GT email:yzhang3026@gatech.edu

from tkinter import *
from tkinter import messagebox
class point:
    def __init__(self,master):

        self.a=[]
        self.b=[]
        self.c=[]
       
        self.count=0

        
        frame=Frame(root)
        frame.pack()
        self.a=Label(frame,text="Number Search File:")
        self.a.grid(row=0,column=0)
        self.b=Label(frame,text="Number Bank File:")
        self.b.grid(row=1,column=0)



        self.v1=StringVar()
        self.v2=StringVar()

        self.e1=Entry(frame,width=100,state='readonly',textvariable=self.v1)
        self.e1.grid(row=0,column=1,)
        self.v1.set('No File Selected')

        self.e2=Entry(frame,width=100,state='readonly',textvariable=self.v2)
        self.e2.grid(row=1,column=1)
        self.v2.set('No File Selected')

        self.sefile1=Button(frame,text='Select File',command=self.openNSClicked)
        self.sefile1.grid(row=0,column=2)
        self.sefile2=Button(frame,text='Select File',command=self.openNBClicked)
        self.sefile2.grid(row=1,column=2)


        self.gesearch=Button(frame,text='Generate Number Search',command=self.generate)
        self.gesearch.grid(row=2,column=0)

    def openNSClicked(self):
        self.filename=filedialog.askopenfilename()
        self.v1.set(self.filename)
        self.readFiles()
        
    def openNBClicked(self):
        self.filename1=filedialog.askopenfilename()
        self.v2.set(self.filename1)
        self.readFiles1()
        
    
    
    def readFiles(self):
       
        import csv
        file=open(self.filename,'r')
        fileread=csv.reader(file)
        fileread2=fileread
        aList=[]
        for row in fileread:
            aList.append(row)

        set1=[]
        
        for i in aList:
            length=len(i)
            for j in i:
                
                nospace=j.strip()
                set1=set1+[nospace]
        avglen=int(len(set1)/(length))
    
        k=0
        set2=[]
        for t in range(avglen):
            f=set1[k:k+length]
            set2.append(f)
            k=k+length
        file.close()

        
        set3=sum(set2,[])
        w=0
        for t in range(len(set3)):
            if set3[t].isdigit()==True or set3[t]=='+' or set3[t]=='*' or set3[t]=='/' or set3[t]=='-':
                w=w+1
        if w!=len(set3):
            messagebox.showerror('Exceuse me!','Invalid file!')
            self.openNSClicked()
        return set2


    def readFiles1(self):
        import csv
        file1=open(self.filename1,'r')
        fileread1=csv.reader(file1)


        w=0
        u=[]
        for t in fileread1:
            if t[0].isdigit()==True or t[0]=='+' or t[0]=='*' or t[0]=='/' or t[0]=='-':
                u.append(t[0])
            else:
                
                w=w+1

        if w!=0:
            messagebox.showerror('Exceuse me!','Invalid file!')
            self.NBClicked()
        return(u)
        
        
        


    def generate(self):
        bigframe=Frame().pack(side=LEFT)


        frame3=Frame(bigframe)
        frame3.pack(side=BOTTOM)
        self.e=Entry(frame3,width=30)
        self.e.pack(side=LEFT)
        
        self.b=Button(frame3,text='Find',command=self.find)
        self.b.pack(side=RIGHT)


        Label(bigframe,text='Have Fun With Math!').pack(side=TOP)
  
        self.u=self.readFiles1()
        
      
        self.frame2=Frame()
        self.frame2.pack(side=RIGHT)

        bigframe=Frame().pack(side=RIGHT)

                                            
        
        for k in range(len(self.u)):
            self.numbersToFind=Label(self.frame2,text=self.u[k],pady=12)
            self.numbersToFind.grid(row=k)
            
        
        
        set2=self.readFiles()
        self.frame1=Frame()
        self.frame1.pack()

        

        for i in range(len(set2)):
            for j in range(len(set2[0])):
                self.numbers=Label(self.frame1,text=set2[i][j], padx = 12 , pady = 12)
                self.numbers.grid(row=i,column=j)


        self.numSearchLines=set2
        
                
        



    def findStartingCoords(self):
        getnum=self.e.get()

        j=0

        while getnum[j].isdigit()==True:
                j=j+1   

        
        firstnum=getnum[0:j]

        y=[]
        for m in range(len(self.numSearchLines)):
            for n in range(len(self.numSearchLines[0])):
                if firstnum==self.numSearchLines[n][m]:
                    y.append((n,m))

        if y==[]:
            messagebox.showwarning('Un oh!','Un oh...chech your math!')
        else:
            return y



        
    def find(self):
        string=self.e.get()
        r=0
        for v in range(len(string)):
            if string[v]=='+' or string[v]=='-' or string[v]=='*' or string[v]=='/':
                r=r+1
        if r!=1:
            messagebox.showwarning('Un oh!','Un oh...chech your math!')

        else:
            try:
                self.calculation=eval(string)
                self.y=self.findStartingCoords()
                self.find2()
                self.findcoord1.append(2)
                del self.findcoord1
                if self.numbersToFind.cget('fg')=='grey':
                    self.count=self.count+1                  
                                         
            except:
                messagebox.showwarning('Un oh!','Un oh...chech your math!')

            if self.count==len(self.u):
                self.a=messagebox.showinfo('Congratulations!',"You've found all the numbers")
            if self.a=='ok':
                root.destroy()
   

    def find2(self):

        
        string=self.e.get()
        for q in range(len(self.y)):
            coord=self.y[q]
            row=coord[0]
            col=coord[1]

            totrow=len(self.numSearchLines)

            totcol=len(self.numSearchLines[0])

            if row>=2 and row<=totrow-3 and col>=2 and col<=totcol-3:
                upfirst=self.numSearchLines[row-1][col]
                upsecond=self.numSearchLines[row-2][col]
                if self.numSearchLines[row][col]+upfirst+upsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row-1,col]
                    self.findcoord2=[row-2,col]
                    self.updateGUI2()
                    self.updateGUI()

                    
                downfirst=self.numSearchLines[row+1][col]
                downsecond=self.numSearchLines[row+2][col]
                
                if self.numSearchLines[row][col]+downfirst+downsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row+1,col]
                    self.findcoord2=[row+2,col]
                    self.updateGUI2()
                    self.updateGUI()
  
                    
                    

                leftfirst=self.numSearchLines[row][col-1]
                leftsecond=self.numSearchLines[row][col-2]
                if self.numSearchLines[row][col]+leftfirst+leftsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row,col-1]
                    self.findcoord2=[row,col-2]
                    self.updateGUI2()
                    self.updateGUI()

                    
                
                rightfirst=self.numSearchLines[row][col+1]
                rightsecond=self.numSearchLines[row][col+2]
                if self.numSearchLines[row][col]+rightfirst+rightsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row,col+1]
                    self.findcoord2=[row,col+2]
                    self.updateGUI2()
                    self.updateGUI()
   


                upleftfirst=self.numSearchLines[row-1][col-1]
                upleftsecond=self.numSearchLines[row-2][col-2]
                if self.numSearchLines[row][col]+upleftfirst+upleftsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row-1,col-1]
                    self.findcoord2=[row-2,col-2]
                    self.updateGUI2()
                    self.updateGUI()



                uprightfirst=self.numSearchLines[row-1][col+1]
                uprightsecond=self.numSearchLines[row-2][col+2]
                if self.numSearchLines[row][col]+uprightfirst+uprightsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row-1,col+1]
                    self.findcoord2=[row-2,col+2]
                    self.updateGUI2()
                    self.updateGUI()


                downleftfirst=self.numSearchLines[row+1][col-1]
                downleftsecond=self.numSearchLines[row+2][col-2]
                if self.numSearchLines[row][col]+downleftfirst+downleftsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row+1,col-1]
                    self.findcoord2=[row+2,col-2]
                    self.updateGUI2()
                    self.updateGUI()
   

                
                downrightfirst=self.numSearchLines[row+1][col+1]
                downrightsecond=self.numSearchLines[row+2][col+2]
                if self.numSearchLines[row][col]+downrightfirst+downrightsecond==string:
                    self.coordorigin=[row,col]
                    self.findcoord1=[row+1,col+1]
                    self.findcoord2=[row+2,col+2]
                    self.updateGUI2()
                    self.updateGUI()
                    
                
           
    

            else:
            
                try:
                    
                    upfirst=self.numSearchLines[row-1][col]
                    upsecond=self.numSearchLines[row-2][col]
                    if row-1<=0 or row-2<=0:
                        upsecond='outofrange'

                    
                    if self.numSearchLines[row][col]+upfirst+upsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row-1,col]
                        self.findcoord2=[row-2,col]
                        self.updateGUI2()
                        self.updateGUI()

                    raise IndexError
                except IndexError:
                   
                    a=2
            
                    
                try:
                    if row+1>len(self.numSearchLines) or row+2>len(self.numSearchLines):
                        downsecond='outofrange'

      
                    downfirst=self.numSearchLines[row+1][col]                  
                    downsecond=self.numSearchLines[row+2][col]

                    
                    if self.numSearchLines[row][col]+downfirst+downsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row+1,col]
                        self.findcoord2=[row+2,col]
                        self.updateGUI2()
                        self.updateGUI()

                    raise IndexError
                except IndexError:
                    
                    a=2
 


                try:
                    leftfirst=self.numSearchLines[row][col-1]
                    leftsecond=self.numSearchLines[row][col-2]
                    if col-1<0 or col-2<0:
                        leftsecond='outofrange'

                    if self.numSearchLines[row][col]+leftfirst+leftsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row,col-1]
                        self.findcoord2=[row,col-2]
                        self.updateGUI2()
                        
                        self.updateGUI()

            
                    raise IndexError
                except IndexError:
                    
                    a=2
                
                try:
                    rightfirst=self.numSearchLines[row][col+1]
                    rightsecond=self.numSearchLines[row][col+2]
                    if col+1>len(self.numSearchLines[0]) or col+1>len(self.numSearchLines[0]):
                        rightsecond='outofrange'

                                                                     
                                 
                    if self.numSearchLines[row][col]+rightfirst+rightsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row,col+1]
                        self.findcoord2=[row,col+2]
                        self.updateGUI2()
                        self.updateGUI()
                        
                        
                    
                    raise IndexError
                except IndexError:
                    
                    a=2
                     
                try:
                    upleftfirst=self.numSearchLines[row-1][col-1]
                    upleftsecond=self.numSearchLines[row-2][col-2]
                    

                    
                    if self.numSearchLines[row][col]+upleftfirst+upleftsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row-1,col-1]
                        self.findcoord2=[row-2,col-2]
                        self.updateGUI2()
                        self.updateGUI()

            
                    raise IndexError
                except IndexError:
                    
                    a=2
                
                try :

                    uprightfirst=self.numSearchLines[row-1][col+1]
                    uprightsecond=self.numSearchLines[row-2][col+2]
                
                    

                    
                    if self.numSearchLines[row][col]+uprightfirst+uprightsecond==string:
                        self.coordorigin=(row,col)
                        self.findcoord1=[row-1,col+1]
                        self.findcoord2=[row-2,col+2]
                        self.updateGUI2()
                        self.updateGUI()

                    raise IndexError
                except IndexError:
                    
                    a=2 
                try:
                    
                    downleftfirst=self.numSearchLines[row+1][col-1]
                    downleftsecond=self.numSearchLines[row+2][col-2]


                        
                    if self.numSearchLines[row][col]+downleftfirst+downleftsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row+1,col-1]
                        self.findcoord2=[row+2,col-2]
                        self.updateGUI2()
                        self.updateGUI()
                    raise IndexError
                except IndexError:
                    
                    a=2
                
                try:
                    
                    downrightfirst=self.numSearchLines[row+1][col+1]
                    downrightsecond=self.numSearchLines[row+2][col+2]


                    if self.numSearchLines[row][col]+downrightfirst+downrightsecond==string:
                        self.coordorigin=[row,col]
                        self.findcoord1=[row+1,col+1]
                        self.findcoord2=[row+2,col+2]
                        self.updateGUI2()
                        self.updateGUI()

                    raise IndexError
                except IndexError:
                    a=2
                    
                
                    
           
        

    def updateGUI(self):
         
        for i in range(len(self.numSearchLines)):
            for j in range(len(self.numSearchLines)):
                if i==self.coordorigin[0] and j==self.coordorigin[1]:
                    self.numbers=Label(self.frame1,text=self.numSearchLines[i][j],bg='yellow', padx = 10 , pady = 10)
                    self.numbers.grid(row=i,column=j)

                if i==self.findcoord1[0] and j==self.findcoord1[1]:
                    self.numbers=Label(self.frame1,text=self.numSearchLines[i][j],bg='yellow', padx = 10 , pady = 10)
                    self.numbers.grid(row=i,column=j)

                if i==self.findcoord2[0] and j==self.findcoord2[1]:
                    self.numbers=Label(self.frame1,text=self.numSearchLines[i][j],bg='yellow', padx = 10 , pady = 10)
                    self.numbers.grid(row=i,column=j)
            
    def updateGUI2(self):
        
        self.t=0
        for k in range(len(self.u)):
            if int(self.u[k])==int(self.calculation):
                self.numbersToFind=Label(self.frame2,text=self.u[k],fg='grey',pady=10)
                self.numbersToFind.grid(row=k)
                self.t=self.t+1


    

  

        1/self.t
       
    
   
       
        
       

root=Tk()
root.title('Number Search Generator!')
p=point(root)
root.mainloop()

    
