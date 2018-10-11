def main():

    def matrix_mult(a,b,c,d,e,f,g,h):
        
        matrix_1=[[a,b],[c,d]]
        matrix_2=[[e,f],[g,h]]

        prod_matrix=[]

        
        prod_element_11=matrix_1[0][0]*matrix_2[0][0]+ \
                        matrix_1[0][1]*matrix_2[1][0]

        prod_element_12=matrix_1[0][0]*matrix_2[0][1]+ \
                        matrix_1[0][1]*matrix_2[1][1]
        
        prod_element_21=matrix_1[1][0]*matrix_2[0][0]+ \
                        matrix_1[1][1]*matrix_2[1][0]
        
        prod_element_22=matrix_1[1][0]*matrix_2[0][1]+ \
                        matrix_1[1][1]*matrix_2[1][1]
        
        prod_row_1=prod_element_11,prod_element_12
        prod_row_2=prod_element_21,prod_element_22

        prod_matrix.append(prod_row_1)
        prod_matrix.append(prod_row_2)

        print(prod_matrix[0],'\n',prod_matrix[1])
        
    a,b = [int(x) for x in input("Enter the first row of matrix 1 seperated by commas, (e.g. 5,8):  ").split(',')]
    c,d = [int(x) for x in input("Enter the second row of matrix 1 seperated by commas:  ").split(',')]
    e,f = [int(x) for x in input("Enter the first row of matrix 2 seperated by commas:  ").split(',')]
    g,h = [int(x) for x in input("Enter the second row of matrix 2 seperated by commas:  ").split(',')]

    matrix_mult(a,b,c,d,e,f,g,h)

    
main()
