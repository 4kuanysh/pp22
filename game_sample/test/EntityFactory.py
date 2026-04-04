import Entity

class EntityFactory:
    
    @staticmethod
    def create_entiry(**kwargs) -> Entity:
        return Entity(Entity.MovementComponent((5, 0)), Entity.RenderComponent([100, 100], [50, 50], (255, 0, 0)))