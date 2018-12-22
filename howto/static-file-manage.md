# django2docs

主编&作者:**蒋乐兴**

wechat:**jianglegege**

email:**1721900707@qq.com**

homepage:**http://www.sqlpy.com**

---

- [什么文件才算是静态文件](#什么文件才算是静态文件)
- [STATIC_URL](#STATIC_URL)
- [在模板中使用static要分两步走](#在模板中使用static要分两步走)
- [STATICFILES_DIRS](#STATICFILES_DIRS)
---


## 什么文件才算是静态文件
   **1): 静态文件在djagno中只有三种 1、css 2、image 3、js 也就是说html模板文件并不会被当成静态文件处理**

   **2): 由于静态文件的物理表现形式是css,image,js也就注定了它是要被用在模板文件中的，如果我们在写模板文件的时候每一次都要自己去“拼写”出一个正确的静态文件的路径这个不现实，这个主要是因为url并不是一成不变的；在模板语言中统一交给static标签来处理**

   ---

## STATIC_URL
   **定义静态文件的统一访问入口，默认值如下**
   ```python
   STATIC_URL = '/static/'
   ```

   ---

## 在模板中使用static要分两步走
   **1): 第一步load static**

   **2): 第二步static 'xxx'**
   ```html
   <htm>
       <!-- 第一步 -->
       {% load static %}
       <head>
           <title>zero's main page</title>
           <style>
               .container {
                   display: flex;
               }
   
               .container img {
                   height: 320px;
               }
           </style>
       </head>
       <body>
           <h1>this is zero main page!</h1>
           <article>
               <div class="container">
                   <!-- 第二步 -->
                   <img src="{% static 'zero/detail-view.png' %}">
               </div>
           </article>
           
       </body>
   </htm>
   ```
   渲染后浏览器看到的html代码
   ```html
   <htm>
       
       <head>
           <title>zero's main page</title>
           <style>
               .container {
                   display: flex;
               }
   
               .container img {
                   height: 320px;
               }
           </style>
       </head>
       <body>
           <h1>this is zero main page!</h1>
           <article>
               <div class="container">
                   <!-- 可以看到效果上就像是静态文件都在/stataic/目录下一样 -->
                   <img src="/static/zero/detail-view.png">
               </div>
           </article>
           
       </body>
   </htm>
   ```

   ---

## STATICFILES_DIRS
   **django查询静态文件的行为就是在每个app的static目录下面找，所以最好是在static目录下在建一个app的同名目录；但是通常情况下有些静态文件是整个项目共用的，这种情况下我们把文件放到哪个app下面都不太好，最好还是保存在项目下，STATICFILES_DIRS就是用来干这个事的，也就是说django还会去找STATICFILES_DIRS列表中指定的目录**
   ```python
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "static"),
   ]
   ```

   ---
