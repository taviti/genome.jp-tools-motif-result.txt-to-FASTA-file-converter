import pandas as pd
import csv
import sys



def swiss():

    

    filename = sys.argv[-1]



    with open('mycsv.csv', 'w') as csvfile:
        with open(filename, 'r') as txtfile:
            txt = csv.reader(txtfile, delimiter = '\t')
    
            out_csv = csv.writer(csvfile)
            out_csv.writerows(txt)
   
   

    df = pd.read_csv('mycsv.csv')
    df1 = []
    for row in df['#ID']:
        j = '>'+row
        df1.append(j)
 
    df['#ID'] = df1
 
   

    df2 =[]
    for row in df['SEQ']:
        j = '#' + row
        df2.append(j)

    df['SEQ'] = df2

   

    df3 = df['#ID']+ df['SEQ']

    print(df3)

    df4 = df3.to_csv('temp.txt', index=False, header=False)
  

def main():

    

    f2 = open('swissfastafile.fasta', 'w')
    with open('temp.txt','r') as f:
 
        for i in f:
        
            if  '#' in i:
                j = i.replace('#', '\n')
                f2.writelines(j)

            else:
               
                f2.writelines(i)
                f2.close()




swiss()



if __name__ == '__main__':
    main()

print("successfully written, Check the output fasta file named 'swissfastafile.txt' in the  same directory, '\n' it only generated if you provide exact result file obtained from motif patter search database https://www.genome.jp/tools/motif/MOTIF2.html")