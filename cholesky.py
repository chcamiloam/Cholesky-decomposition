import math
def start():
  print "A continuacion se recibiran los datos de su matriz, tenga en cuenta que los decimales deben estar separados por un punto(.) y no se admite fracciones. Este metodo solo acepta matriz cuadrada"
        print ""
        n_total= raw_input("ingrese el numero de filas que tendra la matriz: ")
        if n_total=="":
            error()
        list_temp=[]
        list_temp2=[]
        A=U=[[0]*int(n_total) for i in range(int(n_total))]
        for k in xrange(0, int(n_total)):
            for j in xrange(0, int(n_total)):
                num=raw_input("Inserte el numero de la pocision "+str(k+1)+","+str(j+1)+": ")
                        if num=="":
                            error()
                        else:
                            A[k][j]=float(num);
        alert=True
        for k in range(0,int(n_total)):
            for j in range(0,int(n_total)):
                sumatoria=0
                        if k==j:
                            for i in range(0,k):
                                sumatoria+=pow((U[i][k]),2)
                                if (A[k][k]-sumatoria)>=0:
                                    U[k][k]=math.sqrt(A[k][k]-sumatoria);
                                else:
                                    alert=False
                                        print "Hay una raiz negativa, no se puede descomponer"
                        else:
                            if j<k:
                                U[k][j]=0.0
                            else:
                                for i in range(0,k):
                                    sumatoria=sumatoria+(U[i][k]*U[i][j])
                                        U[k][j]=(A[k][j]-sumatoria)/U[k][k]
        if alert:
            print U
def error():
    print "Debe insertar un valor, la aplicacion se cerrara"
        start()
start()
pause = raw_input('Press ENTER to continue')
