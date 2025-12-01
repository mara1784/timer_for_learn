# timer_for_learn
Application where you set how often you want to be notified to take a break.

From the beginning of writing code on my PC, I struggled with how much time 
I should spend time in one piece on improving my programming skills. 
I thought about what I will do for my productivity because I was spending much time in one piece of time without breaks.
Once, I had the idea of creating an application that would determine how long it would take for the program to notify me that I should take a break, and that application is here.

### a) license of my code "Copyright © 2025 Marek Semerák. All rights reserved. The use, modification, and distribution of this code are not permitted without the express written consent of the author. To obtain a license, please contact me."

### b) Third-Party Licenses

This application uses the following third-party software, which is distributed under the terms of the MIT license.

---

### plyer
**Copyright (c) 2010-2022 Kivy Team and other contributors**
https://github.com/kivy/plyer

### ttkbootstrap
**Copyright (c) 2021-2024 Israel Dryer**
https://github.com/israel-dryer/ttkbootstrap

---

### MIT License Text (for the plyer and ttkbootstrap)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



In application I use that imports :  
  import threading  
  from tkinter import font  
  import tkinter as tk  
  from plyer import notification  
  import ttkbootstrap as ttk  
  import time  
  import tkinter  
  from functools import partial  
  from tkinter.scrolledtext import ScrolledText  
  
