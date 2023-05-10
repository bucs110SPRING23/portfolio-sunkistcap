#imports
import pygame

def graph_coordinates(display,iters_dict, max_so_far):
    coordinates = list(iters_dict.items())
    font = pygame.font.Font(None,36)
    
    print(coordinates)
    new_display=pygame.transform.flip(display,False,True)
    width, height = new_display.get_size()
    pygame.draw.lines(new_display,(0,0,255),False,coordinates)
    new_display = pygame.transform.scale(new_display, (width*15 , height*15))
    display.blit(new_display,(0,0))
    msg = font.render(str(max_so_far),True,"red")
    display.blit(msg,(10,10))
    pygame.display.update()

def threenp1range(upper_limit):
    objs_in_sequence={}
    max_so_far=0
    for i in range(2,(upper_limit+1)):
        count=threenp1(i)
        objs_in_sequence[i]= count
        if  count>max_so_far:
            max_so_far=count
    return (objs_in_sequence,max_so_far)

def threenp1(n):
    count=0
    while (n>1):
        count+=1
        if(n%2==0):
            n = int(n/2)
        else:
            n = int(3*n+1)
    return count

def main():
    pygame.init()
    limit=20
    display= pygame.display.set_mode((800,600))
    display.fill((255,255,255))
    (iters_dict,max_so_far)=threenp1range(limit)
    graph_coordinates(display,iters_dict, max_so_far)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.wait(10)
    pygame.quit()
    
if __name__=='__main__':
    main()