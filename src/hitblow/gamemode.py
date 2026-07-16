    print("こんにちはヒットアンドブロー君です！！")
    print("難易度を選んでね♡")
    print("1：かんたん")
    print("2：ふつう")
    print("3：むずかしい")

    while True:
        level = input("選んでください（1～3）：").strip()

        if level == "1":
            digits = 3
            break
        elif level == "2":
            digits = 4
            break
        elif level == "3":
            digits = 5
            break
        else:
            print("1～3で入力してください。")

    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")
