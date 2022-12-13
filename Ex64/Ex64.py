#4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
#https://www.reg.ru ---> www.reg.ru

def circumcision_url (url_str):
    if url_str.find('://')==-1:
        index=0
    else:
        index=url_str.find('://')+3
    if url_str[index:].find('/')==-1:
        url_str+='/'
        end_index=-1
    else:
        end_index=url_str[index:].find('/')+index
    return url_str[index:end_index]

print()
url_list=['https://pythonru.com', 'https://egorovegor.ru', 'https://pythonim.ru']
result=[]
#result_list=[url_list[i][8:] for i in range (0,len(url_list))]
#length_list=len(url_list)
#result_list=list[url_list[i].split('/'[2]+'\n') for int i in range (0,length_lis)]
result=set([circumcision_url(i) for i in url_list] )
print(result)