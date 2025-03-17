import pygame

# Base class for game objects (all objects are circles, even triangle player)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # attribut Player.containters serves for pygame.sprite.Groups
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # find out, if 2 circle shapes are colliding with each other 
    def are_colliding(self, other):
        distance = self.position.distance_to(other.position)
        colliding_distance = self.radius + other.radius
        return distance <= colliding_distance
    
# if __name__ == "__main__":
#     a = CircleShape(1, 1, 1)  
#     b = CircleShape(10, 10, 1)
#     x = a.is_colliding(b)
#     print(f"--- {x}")
