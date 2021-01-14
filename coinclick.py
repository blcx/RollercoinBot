def CoinClick():
    CoinGameover = True
    coin_Click_Game_Clicked = False
    if pyautogui.locateOnScreen('rc_items/CoinClickGame.png', confidence=0.9) != None:
        print("Coin click game start clicked")
        image = pyautogui.locateOnScreen('rc_items/CoinClickGame.png', confidence=0.9)
        if image != None:
            x, y = pyautogui.center(image)
            pyautogui.moveTo(x + 5, y + 20)
            time.sleep(1)
            pyautogui.click()
            CoinGameover = False
            coin_Click_Game_Clicked = True
            time.sleep(3)

    if coin_Click_Game_Clicked == True:
        if pyautogui.locateOnScreen('rc_items/start_game.png', confidence=0.9) != None:
            time.sleep(2)
            Coin_Click_Image_Area = pyautogui.locateOnScreen('GameScreen.png', confidence=0.9)
            print("coin click game area found")

            coin_Click_Game_Clicked = False

            image = pyautogui.locateOnScreen('rc_items/start_game.png', confidence=0.9)
            if image != None:
                x, y = pyautogui.center(image)
                pyautogui.moveTo(x, y)
                time.sleep(1)
                pyautogui.click()
                CoinGameover = False
                Game_Playing = True
                time.sleep(3)

                while CoinGameover == False:

                    pic = pyautogui.screenshot(region=(
                    Coin_Click_Image_Area[0], Coin_Click_Image_Area[1], Coin_Click_Image_Area[2],
                    Coin_Click_Image_Area[3],))
                    width, height = pic.size
                    offsetX = Coin_Click_Image_Area[0]
                    offsetY = Coin_Click_Image_Area[1]  + 10

                    for x in range(0, width, 5):
                        for y in range(0, height, 5):

                            r, g, b = pic.getpixel((x, y))

                            # blue coin
                            if b == 183 and r == 0:
                                click(x + offsetX, y + offsetY)
                                print("blue coin click")

                                break

                            # yellow coin
                            if b == 64 and r == 200:
                                click(x + offsetX, y + offsetY)
                                print("yellow coin click")

                                break

                                # orange coin
                            if b == 33 and r == 231:
                                click(x + offsetX, y + offsetY)
                                print("orange coin click")

                                break

                            # grey coin
                            if b == 230 and r == 230:
                                click(x + offsetX, y + offsetY)
                                print("grey coin click")

                                break

                            # game finish button
                            if b == 228 and r == 3:
                                time.sleep(3)
                                click(x + offsetX, y + offsetY)
                                print("game finish click taking 10 sec wait while verifying")
                                CoinGameover = True

                                print("Game Over = " + str(CoinGameover))

                                time.sleep(3)

                                break

                        if CoinGameover == True:
                            break
                    if CoinGameover == True:
                        Game_Playing = False
                        break





    print("exit from for loop")
    time.sleep(3)
    if pyautogui.locateOnScreen('rc_items/choose_game.png', confidence=0.9) != None:
        image = pyautogui.locateOnScreen('rc_items/choose_game.png', confidence=0.9)
        if image != None:
            print("choose game button pressed")
            x, y = pyautogui.center(image)
            pyautogui.moveTo(x, y)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
