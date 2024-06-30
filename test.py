from mtl import *
from mtl.css import *

import mtl.tags as t


def Nav(props):
    return pack(
        nav(
            ul(
                li(h1("mtl", props=[className("mtl nav-icon")])),
                li(a("Home", props=[href("#")])),
            ),
            ul(li(a("Login")), li(a("Register"))),
            props=[
                onClick("""console.log('Hello HTML In Python')"""),
                className("MainNav"),
                props,
            ],
        ),
        styles(
            """
                .MainNav {
                    display: flex;
                    align-items: center;
                    gap: 15px;
                    justify-content: space-between;
                    background-color: rgba(255, 255, 255, 0.884);
                    padding: 0px;
                    border-radius: 10px;
                    z-index: 9;
                    font-family: "Nunito";
                    padding: 16px;
                    user-select: none;
                    backdrop-filter: blur(15px);

                    ul {
                        display: flex;
                        align-items: center;
                        gap: 15px;

                        li {
                            list-style-type: none;

                            a {
                                cursor: pointer;
                                font-size: 18px;
                                font-weight: 600;
                                text-decoration: none;
                                color: black;
                            }
                        }
                    }
                }
            """
        ),
    )


def Poppins(kwrgs, *content):
    return t.htm(kwrgs, *content, props=[style("font-family: 'Poppins'")], ref="")


TestComp = div(
    Poppins("h1", "Test Component"),
    props=[
        style(
            "height: 50%; display: flex; align-items: center; justify-content: center;"
        )
    ],
)

TestComp2 = pack(
    div(
        Poppins(
            "h1",
            "Test Components 1"
        ),
        Poppins(
            "h1",
            "Test Components 2"
        ),
        props=[
            style(
                useMtlCss([
                    dis("flex"),
                ]),

            )
        ]
    ),
    div(
        Poppins(
            "a",
            a(
                "https://www.weareinspace.net",
                props=[
                    href("https://www.weareinspace.net")
                ]
            )
        )
    )
)

Home = pack(
    head(
        styles(
            """
                @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Playfair:ital,opsz,wght@0,5..1200,300..900;1,5..1200,300..900&display=swap');

                * {
                    padding: 0;
                    margin: 0;
                    box-sizing: border-box;
                }

                body {
                    background: #f6f5f2;
                }

                .cont {
                    padding-left: 18vw;
                    padding-right: 18vw;
                }

                @media screen and (max-width: 1024px) {
                    .cont {
                        padding-left: 16vw;
                        padding-right: 16vw;
                    }
                }

                @media screen and (max-width: 770px) {
                    .cont {
                        padding-left: 8vw;
                        padding-right: 8vw;
                    }
                }

                @media screen and (max-width: 640px) {
                    .cont {
                        padding-left: 16px;
                        padding-right: 16px;
                    }
                }

                .nav-cont-cont {
                    position: sticky;
                    top: 0;
                    padding-top: 16px;
                    padding-bottom: 16px;
                }

                .mtl {
                    text-decoration: none;
                    font-optical-sizing: auto;
                    font-weight: 500;
                    font-style: italic;
                    font-size: 40px;
                    margin-right: 10px;
                    line-height: 1;
                    font-family: "lora";
                }
            """,
            """
                a {
                    
                }
            """,
        ),
        script(
            """
                function Hello() {
                    console.log('Hello HTML from Python')
                }
            """
        ),
    ),
    body(
        div(
            Nav(onClick("Hello()")),
            TestComp,
            TestComp2,
            props=[
                className("cont nav-cont-cont")
            ]
        )
    ),
)

f = open("doc.html", "a")
f.truncate(0)
f.write(Home)
f.close()
