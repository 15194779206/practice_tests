import pickle
def data():
    main_dict = {
        "北京分校": {
            "python": {
                "teacher": "金角大王",
                "grade": "金角一班"
            },
            "linux": {
                "teacher": "银角大王",
                "grade": "银角一班"
            },
            "上海校区": {
                "go": {
                    "teacher": "唐僧",
                    "grade": "唐僧一班"
                },
            }

        }
    }
    f = open("main_dict.text", "wb")
    pickle.dump(main_dict, f)

    teacher_dict = {
        "金角大王": {
            "grade": "金角一班"
        },
        "银角大王": {
            "grade": "银角一班"
        },
        "唐僧": {
            "grade": "唐僧一班"
        }
    }
    f = open("teacher_dict.text", "wb")
    pickle.dump(teacher_dict, f)

data()