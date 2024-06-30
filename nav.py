from mtl import *

def Nav(props):
    return(
        pack(
            nav(
                ul(
                    li(
                        h1(
                            "mtl",
                            props=[
                                className("mtl nav-icon")
                            ]
                        )
                    ),
                    li(
                        a(
                            "Home",
                            props=[
                                href("#")
                            ]
                        )
                    )
                ),
                ul(
                    li(
                        a("Login")
                    ),
                    li(
                        a("Register")
                    )
                ),
                props=[
                    onClick('''console.log('Hello HTML In Python')'''),
                    className("MainNav"),
                    props
                ]
            ),
            styles(
                '''
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
                '''
            )
        )
    )