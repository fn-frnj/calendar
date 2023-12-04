#!/usr/bin/env python
# coding: utf-8

# ## AS3006 - Sistem Kalender - Menghitung hari
# Farah Najla / 10319006

# In[ ]:


#dt1 = 1 Januari 2000, dt2 = input date
dt1 = [1, 1, 2000]


# In[ ]:


inputdate = input("DD-MM-YYYY = ")
#inputdate = "04-12-2023"


# In[ ]:


arr_date= inputdate.split("-")
dt2 = list(map(int, arr_date))


# In[ ]:


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


# In[ ]:


monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #belum memperhitungkan leap year


# In[ ]:


# hari karena Leap Year sebelum dt1
lydt1 = int(1999 / 4) - int(1999 / 100) + int(1999 / 400)
# hari karena Leap Year sebelum dt2
lydt2 = int(dt2[2] / 4) - int(dt2[2] / 100) + int(dt2[2] / 400)


# In[ ]:


def getDifference(dt1, dt2):
 
    n1 = dt1[2] * 365 + dt1[0]
 
    for i in range(0, dt1[1] - 1):
        n1 += monthDays[i]
 
    n1 += lydt1 #tambahkan hari karena leap year
 
    n2 = dt2[2] * 365 + dt2[0]
    for i in range(0, dt2[1] - 1):
        n2 += monthDays[i]
    n2 += lydt2 #tambahkan hari karena leap year
 
    return (n2 - n1)


# In[ ]:


#diketahui 1 Januari 2000 hari Sabtu
x = getDifference(dt1,dt2)


# In[ ]:


dx = x % 7
if dx == 1:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Minggu") #1 hari setelah Sabtu
elif dx == 2:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Senin") #2 hari setelah Sabtu
elif dx == 3:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Selasa") #3 hari setelah Sabtu
elif dx == 4:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Rabu") #4 hari setelah Sabtu
elif dx == 5:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Kamis") #5 hari setelah Sabtu
elif dx == 6:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Jumat") #6 hari setelah Sabtu
if dx == 0:
    print("Tanggal ", dt2[0],"/", dt2[1], "/", dt2[2], " adalah hari Sabtu") #7 hari setelah Sabtu

