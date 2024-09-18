from flet import *

def main(page:Page):
    page.title= "mouayad"
    page.window.height= 740
    page.window.width =390
    page.window.top = 10
    page.window.left = 960
    page.theme_mode = ThemeMode.LIGHT
    
    def route_change(route):
        page.views.clear()
        
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title = Text("MZH"),
                        color = 'white',
                        bgcolor=colors.CYAN_ACCENT_200
                        ),
                    Text('Welcome...',size=24,color='black',width=370,text_align='center'),
                    Row([
                        Image(src="Animated-GIF-Banana.gif",width=240)
                    ],alignment=MainAxisAlignment.CENTER),
                    Text("اهلا وسهلا بك",size=15,color='CYAN',width=370,text_align='center'),
                    Row([
                        ElevatedButton(
                            "تسجيل دخول",
                            width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white'),
                            
                            on_click=lambda _: page.go("/login")),
                    ElevatedButton(
                        "انشاء حساب",
                                    width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white')
                            
                                   ,on_click=lambda _: page.go("/signup")),
                        
                    ],alignment=MainAxisAlignment.CENTER),
                    
                ],
                )
        )
    
    
        if page.route == "/login":
            page.views.append(
            View(
                "/login",
                [
                     AppBar(
                        title = Text(" صفحة تسجل دخول"),
                        color = 'white',
                        bgcolor=colors.CYAN_ACCENT_200
                        ),
                    Text(" ❤😍 اهلا وسهلا بعودتك",size=15,color='CYAN',width=370,text_align='center'),
                    TextField(label='email : البريد'),
                    TextField(label='password : كلمة المرور'),
                    Row([
                        ElevatedButton(
                            "تسجيل دخول",
                            width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white')
                            
                            ),
                    ElevatedButton(
                        "انشاء حساب",
                                    width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white'),
                            
                                   on_click=lambda _: page.go("/signup")),
                        
                    ],alignment=MainAxisAlignment.CENTER),
                ],
            )
            )
            
        if page.route == "/signup":
            page.views.append(
            View(
                "/signup",
                [
                    AppBar(
                        title = Text(" صفحة انشاء حساب جديد"),
                        color = 'white',
                        bgcolor=colors.CYAN_ACCENT_200
                        ),
                   Text(" ❤😍 انشاء حساب ",size=15,color='CYAN',width=370,text_align='center'),
                   TextField(label='email : البريد'),
                   TextField(label='full name : الاسم الكامل'),
                   TextField(label='password : كلمة المرور'),
                   TextField(label='password :  تأكيد كلمة المرور'),
                   Row([
                        ElevatedButton(
                            "انشاء حساب",
                            width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white')
                            
                            ),
                    ElevatedButton(
                        "هل لديك حساب ؟",
                                    width=170,
                            style=ButtonStyle(bgcolor='cyan',color='white'),
                            
                                   on_click=lambda _: page.go("/login")),
                        
                    ],alignment=MainAxisAlignment.CENTER),
                ],
                )
        )
        page.update()
        
    def page_go(view):
        page.views.pop()
        back_page = page.views[-1]
        page.go(back_page.route)
    
    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)
    
    
    
app(main)
