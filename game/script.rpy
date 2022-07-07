style ruby_style is default:
    size 24
    yoffset -42

style say_dialogue:
    line_leading 12
    ruby_style style.ruby_style

$ first = True

# 角色定义 ----------------------------------------------------------------------
define n = Character("尼禄", image="nero", who_color="#00A3FF")

# 开场画面 ----------------------------------------------------------------------

label splashscreen:
    image pure_white =  "#ffffff"

    show pure_white
    show logo at truecenter with Dissolve(1.0)
    pause(1.0)
    hide logo with Dissolve(1.0)

    pause (1.0)

    $ renpy.movie_cutscene("opening.mpg")

    return

# 主菜单之前 --------------------------------------------------------------------

# label before_main_menu:
#
#     return

# 主菜单 -----------------------------------------------------------------------

# label main_menu:
#
#     return

# 游戏主题

label start:

    scene bg bench morning

    play music bgm fadeout 1.0 fadein 1.0

    "这是一个旁白"

    "我能说话"

    show nero normal

    n "余是{rb}尼禄・克劳狄乌斯・凯萨・奥古斯都・日耳曼尼库斯{/rb}{rt}ネロ・クラウディウス・カエサル・アウグストゥス・ゲルマニクス{/rt}，罗马帝国的皇帝。"

    n "汝为何人?"

    $ name = renpy.input("请告诉尼禄你的名字：", length=10).strip()

    n happy "幸会，[name]！"

    scene bg moonlight
    with fade

    hide nero normal
    show nero shy

    n "汝知道余的生日吗？"

    menu:

        "知道哦！是12月15日":

            call know from _call_know

        "啊，抱歉，我不知道":

            call d_know from _call_d_know

    "（Demo完）"

    return


label know:

    show nero happy

    n "太好了！你果然知道"

    hide nero happy

    return


label d_know:

    show nero shy

    n "可恶！"

    hide nero shy

    return
