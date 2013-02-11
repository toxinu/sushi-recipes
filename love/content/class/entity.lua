local Entity = class {x=5,y=5}

function Entity:__init(x,y)
  self.class = "Entity"
  self.x = tonumber(x)
  self.y = tonumber(y)
end

function Entity:draw()
end

function Entity:update(dt)
  assert(dt, "Update method need dt")
end

return Entity
