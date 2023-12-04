#!/usr/bin/env python
# coding: utf-8

# ## Tugas Konversi Gregorian - Hijriyah
# Farah Najla / 10319006

# In[1]:


# Input Tanggal Hijriyah 1 SYAWAL 1443
# Input Tanggal Gregorian
hy = 1443
hm = 10
hd = 1


# In[2]:


import math
N = hd + math.floor(29.5001*(hm-1)+0.99)
Q = math.floor(hy/30)
R = hy%30
A = math.floor((11*R+3)/30)
W = 404*Q + 354*R + 208 + A
Q1 = math.floor(W/1461)
Q2 = W%1461
G = 621 + 4*math.floor(7*Q+Q1)
K = math.floor(Q2/365.2422)
E = math.floor(365.2422*K)
J = Q2 - E + N - 1
X = G + K


# In[3]:


if J > 366 and X%4 == 0:
    J = J - 366
    X = X + 1
elif J > 365 and X%4 > 0:
    J = J - 365
    X = X + 1
# J Nomor hari di Julian dates


# In[4]:


JD = math.floor(365.25*(X-1)) + 1721423 + J
alp = math.floor((JD-1867216.25)/36524.25)
beta = JD + 1 + alp - math.floor(alp/4)
if JD < 2299161:
    beta = JD
b = beta + 1524
c = math.floor((b-122.1)/365.25)
d = math.floor(365.25*c)
e = math.floor((b-d)/30.6001)


# In[5]:


GD = b - d - math.floor(30.6001*e)
if e < 14:
    GM = e - 1
else:
    GM = e - 13


# In[6]:


if GM > 2:
    GY = c - 4716
else:
    GY = c - 4715


# In[7]:


print(GD,GM,GY)


# In[8]:


if ((11*R +3)%30) > 18:
    print('Tahun Hijriyah kabisat')
else:
    print('Tahun Hijriyah biasa')


# Jadi 1 Syawal 1443 Hijriyah jatuh pada tanggal 3 Mei Gregorian

# In[9]:


# Input Tanggal Gregorian
gy = 2022
gm = 8
gd = 17


# In[10]:


if gm <3:
    gy = gy -1
    gm = gm +12


# In[11]:


alp = math.floor(gy/100)
beta = 2 - alp + math.floor(alp/4)
b = math.floor(365.25*gy) + math.floor(30.6001*(gm+1)) + gd + 1722519 + beta
c = math.floor((b-122.1)/365.25)
d = math.floor(365.25*c)
e = math.floor((b-d)/30.6001)
JD = b - d - math.floor(30.6001*e)


# In[12]:


if e < 14:
    JM = e -1
else:
    JM = e -13


# In[13]:


if JM > 2:
    JY = c - 4716
else:
    JY = c - 4715


# In[14]:


if JY%4 == 0:
    W = 1
else:
    W = 2


# In[15]:


N = math.floor(((275*JM)/9)) - W * math.floor((JM+9)/12) + JD - 30
A = JY - 623
B = math.floor(A/4)
C = A%4
C1 = 365.2501*C
C2 = math.floor(C1)
if (C1-C2) == 0.5:
    C2 = C2+1


# In[24]:


D = 1461*B + 170 + C2
Q = math.floor(D/10631)
R = D%10631
J = math.floor(R/354)
K = R%354
O = math.floor((11*J + 14)/30)


# In[25]:


HY = 30*Q + J + 1
DayNum = K - O + N -1
if DayNum > 354:
    CL = HY%30
    DL = (11*CL +3)%30
    if DL < 19:
        DayNum = DayNum - 354
        HY = HY+1
    elif DL < 18:
        DayNum = DayNum - 355
        HY = HY+1
elif DayNum == 0:
    DayNum = 355
    HY = HY-1


# In[26]:


S = math.floor((DayNum-1)/29.5)
HM = 1 + S
HD = math.floor(DayNum - 29.6*S)
if DayNum == 355:
    HM = 12
    HD = 30


# In[27]:


HD, HM, HY


# Maka 17 Agustus 2022 Gregorian jatuh pada 18 Muharram 1441
