import pygame
import random # 랜덤으로 사과 띄움
import time
from datetime import datetime
from datetime import timedelta
from tkinter import *
# import tkinter.messagebox

pygame.init() # pygame 초기화

SCREEN_WIDTH = 440 # 화면 너비
SCREEN_HEIGHT = 440 # 화면 높이
BLOCK_SIZE = 20 # 블록 크기(네모 한칸 크기)
# 화면의 가로세로가 400이고 블록의 크기가 20이기 때문에 가로, 세로는 20칸씩 블록이 들어갈 수 있다.

# 화면의 테두리부분 영역
EDGE = []
for w in range(0, 22) :
    EDGE.append((0, w))
    EDGE.append((21, w))
    EDGE.append((w, 0))
    EDGE.append((w, 21))

# 시작 버튼 영역
START = []
for s in range(0, 8) :
    START.append((SCREEN_WIDTH // 22 * 7 + BLOCK_SIZE * s, SCREEN_HEIGHT // 2 + BLOCK_SIZE // 2))
    START.append((SCREEN_WIDTH // 22 * 7 + BLOCK_SIZE * s, SCREEN_HEIGHT // 2 + BLOCK_SIZE // 2 + BLOCK_SIZE))
    START.append((SCREEN_WIDTH // 22 * 7 + BLOCK_SIZE * s, SCREEN_HEIGHT // 2 + BLOCK_SIZE // 2 + BLOCK_SIZE * 2))

# 색
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SNAKEGREEN = (29, 139, 21)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BROWN = (124, 56, 0)

# 점수
score = 0
# pygeme.display.set_mode((화면 너비, 화면 높이)) 화면 객체 반환
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('SnakeGame') # title 설정

# 화면
# 시작 화면
def draw_main(screen) :
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)
    # 시작버튼
    for start in START :
        startButton = pygame.Rect((start[0], start[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, GREEN, startButton)
    # 시작글씨
    font = pygame.font.Font('freesansbold.ttf', BLOCK_SIZE * 2) # 폰트 설정
    text = font.render('start!', True, BLACK) # 글자 설정 render('출력', True, 글자색, 배경색)
    textRect = text.get_rect()
    textRect.center = (int(((SCREEN_WIDTH // 4) + (BLOCK_SIZE * 5.5))), ((SCREEN_HEIGHT // 2) + (BLOCK_SIZE * 2)))
    screen.blit(text, textRect)
    
    # 제목
    title_font = pygame.font.Font('freesansbold.ttf', BLOCK_SIZE * 3) # 폰트 설정
    title_text = title_font.render('Snake Game', True, SNAKEGREEN) # 글자 설정 render('출력', True, 글자색, 배경색)
    title_textRect = title_text.get_rect()
    title_textRect.center = (int(((SCREEN_WIDTH // 4) + (BLOCK_SIZE * 5.5))), (SCREEN_HEIGHT // 3))
    screen.blit(title_text, title_textRect)

# 게임 배경
def draw_background(screen) :
    # 화면 전체에 강과 땅을 그려준다.
    # pygame.Rect((x, y), (사각형 너비, 사각형 높이))
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.draw.rect(사각형을 그릴 화면, 색, 사각형 정보)
    pygame.draw.rect(screen, BROWN, background)
    # 테두리는 파란색으로 칠해준다.
    for edge in EDGE :
        edges = pygame.Rect((edge[0] * BLOCK_SIZE, edge[1] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, BLUE, edges)


# 블록을 그리는 함수 이 함수로 뱀이나 사과같은것들을 그려준다.
def draw_block(screen, color, position) :
    # position[n] * BLOCK_SIZE는 블록의 위치를 나타낸다.
    # 화면크기가 400*400, 블록이 20*20이기 때문에 화면은 가로, 세로 20칸이 된다. x, y를 이를 이용해 설정한것
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


# 블록 위치 = 뱀이 처음 나올 위치
block_position = [9, 9]
# 마지막으로 블록을 움직인인 때 = 마지막으로 버튼을 누른 때
# datetime.now()는 현재 시간을 알려준다.
last_moved_time = datetime.now()
# 처음 블록의 방향은 아래
block_direction = 'down'

# 방향 키 입력에 따라 블록의 방향 dictionary
DIRECTION_ON_KEY = {
    pygame.K_UP : 'up',
    pygame.K_DOWN : 'down',
    pygame.K_LEFT : 'left',
    pygame.K_RIGHT : 'right'
}

# 뱀
class Snake :
    color = GREEN
    # speed = 0.3
    def __init__(self) :
        self.positions = [(11, 11)] # 뱀의 위치. 뱀이 길어질수록 이 배열도 길어질것이다.
        self.direction = 'down' # 뱀의 방향
        self.speed = 0.3

    def draw(self, screen) :
        # 뱀그리기. 사과를 먹을수록 길어져야한다.
        # 여러 블록으로 이루어져있기 때문에 반복문을 돌며 그린다.
        for position in self.positions:
            draw_block(screen, self.color, position)
    # 뱀이 움직이면 머리가 움직인것에 따라 꼬리까지 따라가게 만드는 함수
    def crawl(self) :
        # 뱀의 머리는 인스턴스 변수인 positions[0] 위치이다.
        head_position = self.positions[0]
        # x, y 변수에 머리의 x, y좌표를 넣어준다.
        x, y = head_position
        # 만약 현재 뱀이 움직이는 방향이 아래라면
        if self.direction == 'down' :
            # 뱀의 머리 위치를 한칸 아래로 바꿔주고,
            # 기존 뱀의 위치 중 꼬리가 있던 부분 직전까지 더해준다.
            # 이렇게하면 머리의 위치를 앞에 추가해줌으로써
            # 머리부터 꼬리까지 각자 블럭의 앞에 있던 칸으로 따라간다.
            self.positions = [(x, y + 1)] + self.positions[:-1]
        elif self.direction == 'up' :
            self.positions = [(x, y - 1)] + self.positions[:-1]
        elif self.direction == 'left' :
            self.positions = [(x - 1, y)] + self.positions[:-1]
        elif self.direction == 'right' :
            self.positions = [(x + 1, y)] + self.positions[:-1]
    # 뱀의 방향을 바꾸는 함수
    def turn(self, direction) :
        self.direction = direction
    # 뱀을 키워주는 함수
    def grow(self) :
        # 뱀 꼬리의 뒤에 한칸 붙여준다.
        x, y = self.positions[-1]
        if self.direction == 'up' :
            self.positions.append((x, y - 1))
        elif self.direction == 'down' :
            self.positions.append((x, y + 1))
        elif self.direction == 'left' :
            self.positions.append((x - 1, y))
        elif self.direction == 'right' :
            self.positions.append((x + 1, y))
        # 뱀의 속도를 높여준다.
        if len(self.positions) > 15  and len(self.positions) < 25  :
            self.speed = 0.2
        elif len(self.positions) > 25 :
            self.speed = 0.1        

# 사과
class Apple :
    color = RED
    def __init__(self, position = (7, 7)) :
        self.position = position # 사과 위치

    def draw(self, screen) :
        # 사과 그리기
        draw_block(screen, self.color, self.position)    

# 게임판 : 뱀과 사과를 그려준다
class Board :
    width = 20
    height = 20
    
    def __init__(self) :
        self.snake = Snake()
        self.apple = Apple()

    def draw(self, screen) :
        self.apple.draw(screen) # 게임판 위의 사과 그리기
        self.snake.draw(screen) # 게임판 위의 뱀 그리기
    # 사과 만들기 - 사과에 사과만들기를하면 snake인스턴스를 못쓴다.
    def put_new_apple(self) :
        # 0 부터 20까지 랜덤으로 수를 정해 사과 위치를 정한다.
        self.apple = Apple((random.randint(1, 20), random.randint(1, 20)))
        # 뱀의 몸과 겹치면 사과를 다시만든다.
        for position in self.snake.positions :
            if self.apple.position == position :
                self.put_new_apple()
                break
    # 시간이 지나면 process_turn 메소드가 실행되며 저절로 뱀이 움직인다.
    def process_turn(self) :
        self.snake.crawl()
        # 뱀머리가 몸이나 벽에 부딛히면 게임이 끝난다.
        if self.snake.positions[0] in self.snake.positions[1:] or self.snake.positions[0] in EDGE:
            play = False
            return play
            
        # 움직이다가 사과 == 뱀머리 이면 뱀을 길게만들고 새 사과를 만든다.
        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()
            self.put_new_apple()
            return 1
        return 1
    # 점수를 표시해주는 메소드.
    def write_score(self, screen) :
        score = 'score : {}'.format(len(self.snake.positions) - 1)
        # 상단에 점수표시
        font = pygame.font.Font('freesansbold.ttf', BLOCK_SIZE) # 폰트 설정
        text = font.render(score, True, BLACK, WHITE) # 글자 설정 render('출력', True, 글자색, 배경색)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, BLOCK_SIZE // 2)
        screen.blit(text, textRect)    

class Play_Again :
    replay = True    
    def __init__ (self, replay) :
        # 윈도우 창 생성
        replay_window = Tk()
        # 윈도우 창 타이틀 지정
        replay_window.title('Game Over')
        # 윈도우 창의 크기 지정
        replay_window.geometry('230x100')
        # 윈도우 창 크기변경 가능?
        replay_window.resizable(0, 0)
        # 라벨
        show_text = Label(replay_window, text='~Game Over~\n다시하시겠습니까?').place(x = 60, y = 15)
        # 버튼
        replay_btn = Button(replay_window, text='Play Again', command = lambda: (self.Play(replay), replay_window.destroy())).place(x = 40, y = 60)
        exit_btn = Button(replay_window, text='Exit', command = lambda: (self.End(replay), replay_window.destroy())).place(x = 150, y = 60)
        # 윈도우 창 유지
        replay_window.mainloop()
        
    def Play(self, replay) : 
        self.replay = True
        return self.replay

    def End(self, replay) :
        self.replay = False
        return self.replay

# 처음시작?
first = True
# 재시작?
replay = True
# 게임실행
play = True


"""반복문 + 게임판을 함수에 넣고 시작버튼을 누르면 반복되고, 종료를 누르면 종료되도록?"""
while replay :
    if first == True :
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        draw_main(screen)
        pygame.display.update()
        events = pygame.event.get()
        for event in events :
            # 마우스 up 이벤트
            if event.type == pygame.MOUSEBUTTONUP :
                print(pygame.mouse.get_pos())
                
                first = False
                board = Board()
                # 종료를 누르기 전까진 화면을 계속 보여준다.
                while play :
                    # pygame.event.get() 발생한 이벤트 목록을 읽는다.
                    events = pygame.event.get()
                
                    # 반복문을 이용하여 이벤트 목록을 본다.
                    for event in events :
                        # 종료 이벤트가 발생하면 종료한다.
                        if event.type == pygame.QUIT :
                            # exit()
                            pygame.quit()
                        # 어떤 버튼을 눌렀다면 아래처럼 행동한다.
                        if event.type == pygame.KEYDOWN :
                            # 만약 눌린 버튼이 화살표키라면 블록의 방향을 화살표 키에 맞게 바꾼다.
                            if event.key in DIRECTION_ON_KEY :
                                # dictionary
                                board.snake.turn(DIRECTION_ON_KEY[event.key])
                
                    # datetime.now() - last_moved_time을 이용하여 마지막으로 버튼을 누른지 0.3초가 지났다면
                    # timedelta() 두 날짜(일,주 등등)나 시간(초, 분 등등)의 차이를 알려준다.
                    if timedelta(seconds = board.snake.speed) <= datetime.now() - last_moved_time :
                        play = board.process_turn()
                        last_moved_time = datetime.now() # 마지막으로 움직인 시간 알려줌
                
                    draw_background(screen) # 배경그리기
                    board.draw(screen) # 화면판에 게임판그리기
                    board.write_score(screen)
                    
                    # 화면 새로고침
                    pygame.display.update()
                if not play :
                    # 게임이 종료되면 play == False가 되며 while을 빠져나온다.
                    play_again = Play_Again(replay)
                    replay = play_again.replay
                    if replay :
                        # 만약 재시작을 한다고 했다면 play = True가 되며 다시 게임이 시작된다.
                        play = True
                        continue
                    # 하지만 재시작을 하지 않는다 했다면 반복문은 종료된다.
                    break
    else :
         board = Board()
            
         # 종료를 누르기 전까진 화면을 계속 보여준다.
         while play :
            # pygame.event.get() 발생한 이벤트 목록을 읽는다.
            events = pygame.event.get()
            
            # 반복문을 이용하여 이벤트 목록을 본다.
            for event in events :
                # 종료 이벤트가 발생하면 종료한다.
                if event.type == pygame.QUIT :
                    # exit()
                    pygame.quit()
                # 어떤 버튼을 눌렀다면 아래처럼 행동한다.
                if event.type == pygame.KEYDOWN :
                    # 만약 눌린 버튼이 화살표키라면 블록의 방향을 화살표 키에 맞게 바꾼다.
                    if event.key in DIRECTION_ON_KEY :
                        # dictionary
                        board.snake.turn(DIRECTION_ON_KEY[event.key])
            
            # datetime.now() - last_moved_time을 이용하여 마지막으로 버튼을 누른지 0.3초가 지났다면
            # timedelta() 두 날짜(일,주 등등)나 시간(초, 분 등등)의 차이를 알려준다.
            if timedelta(seconds = board.snake.speed) <= datetime.now() - last_moved_time :
                play = board.process_turn()
                last_moved_time = datetime.now() # 마지막으로 움직인 시간 알려줌
                
            draw_background(screen) # 배경그리기
            board.draw(screen) # 화면판에 게임판그리기
            board.write_score(screen)
                
            # 화면 새로고침
            pygame.display.update()
         if not play :
            # 게임이 종료되면 play == False가 되며 while을 빠져나온다.
            play_again = Play_Again(replay)
            replay = play_again.replay
            if replay :
                # 만약 재시작을 한다고 했다면 play = True가 되며 다시 게임이 시작된다.
                play = True
                continue
            # 하지만 재시작을 하지 않는다 했다면 반복문은 종료된다.
            break

        
   
# 게임도 종료된다. exit()
pygame.quit()
    
