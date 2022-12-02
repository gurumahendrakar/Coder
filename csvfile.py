string_ = '2+2+6+63*2*3+6*6'
print(len(string_))

print(string_)
operator_index = []
new_string = ''
onemore_stirng_ = ''
twomore_string = ''

class Ool:

    def ___indexfinder(self,string):

        storer = []
        for index,i in enumerate(string):
            if i in '/+-*':
                storer.append(onemore_stirng_.index(i,index))

        else:
            return storer

    def spliting(self):
        global  new_string
        for txt in string_:
            if txt in '*/-+':
                new_string += '-'
            else:
                new_string += txt

    def indexing_adder(self):
        for index, i in enumerate(string_):
            if i in '+/-*':
                operator_index.append(string_.index(i, index))

    def devide_cal(self,index_list: list):
        global onemore_stirng_
        one_time = True

        x,y,idx_counter = 0,1,0
        devide_couting = 0
        count = 0
        while idx_counter<len(index_list):

            if string_[operator_index[idx_counter]]=='/':
                if operator_index[-1] == string_.index(string_[operator_index[idx_counter]],operator_index[idx_counter]):
                    onemore_stirng_ = onemore_stirng_[:self.___indexfinder(onemore_stirng_)[-1]]

                    onemore_stirng_+= string_[operator_index[idx_counter-(count+1)]] + str(numbers_index[x] / numbers_index[y])


                if y<=len(numbers_index)-2:

                    if string_[operator_index[idx_counter+1]]=='/':
                        count+=1
                        devide_couting = numbers_index[x] / numbers_index[y]
                        numbers_index[y] = devide_couting

                    else:
                        if self.___indexfinder(onemore_stirng_):
                            onemore_stirng_ = onemore_stirng_[:self.___indexfinder(onemore_stirng_)[-1]]

                            if count==0:
                                onemore_stirng_+= string_[operator_index[idx_counter-1]] +   str(numbers_index[x] / numbers_index[y])

                            else:
                                onemore_stirng_ += string_[operator_index[idx_counter - (count+1)]] + str(numbers_index[x] / numbers_index[y])
                                count = 0
                        else:
                            onemore_stirng_+= str(numbers_index[x] / numbers_index[y])

            else:
                if one_time:
                    one_time = False
                    onemore_stirng_+=  str(numbers_index[x]) + str(string_[operator_index[idx_counter]]) + str(numbers_index[y])
                else:
                    onemore_stirng_+= str(string_[operator_index[idx_counter]]) + str(numbers_index[y])

            x,y = x+1,y+1
            idx_counter+=1

    def multiply(self,string__):
        global  onemore_stirng_
        new_st = onemore_stirng_
        number_index = []
        allop = []


        for ix in range(len(onemore_stirng_)):
            if onemore_stirng_[ix] in '*-+':
                allop.append(onemore_stirng_.index(onemore_stirng_[ix],ix))


        else:
            for ixx in onemore_stirng_:
                if ixx in '*+-':
                    new_st = new_st.replace(ixx,'-')


            print("Hello Brother : > ",allop)

            allnumxx = list(map(lambda x : float(x) if '.' in x else int(x) ,new_st.split('-')))

            print("Allnumxxx     : > ",allnumxx)

        x,y,count,stringg,multiplyy = 0,1,0,'',0

        while count<=len(allop)-1:

            if onemore_stirng_[allop[count]]=='*':

                if count<len(allop)-1:
                    print('coming multiply',x,y,multiplyy,count)

                    if onemore_stirng_[allop[count+1]] == '*':
                        multiplyy  += allnumxx[x] * allnumxx[y]
                        print('result',multiplyy)


                    else:
                        print('Im here Brother')
                        multiplyy = multiplyy * allnumxx[y]
                        stringg += str(multiplyy)
                        multiplyy = 0



                else:
                    print('last checking',multiplyy,x,y)
                    stringg+= str(multiplyy * allnumxx[y])

            else:
                pass


            x+=1
            y+=1
            count+=1
        print(stringg)



Oo = Ool()
Oo.spliting()
Oo.indexing_adder()
import time

a = time.time()
try:
    numbers_index = list(map(int,new_string.split('-')))
    Oo.devide_cal(operator_index)

    print(onemore_stirng_,'Len',len(onemore_stirng_))
    print(eval(onemore_stirng_.strip('+')))
    print(eval(string_))
    string_ = ''
except:
    raise ValueError('Please Check Giving Value')
# print(time.time()-a)


Oo.multiply(onemore_stirng_)

