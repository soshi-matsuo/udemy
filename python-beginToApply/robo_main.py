from roboter.Robot import Robot

def main():
    robo = Robot()
    human_name = robo.ask_name()
    robo.recommend()
    robo.ask_restaurant(human_name)

if __name__ == '__main__':
    main()