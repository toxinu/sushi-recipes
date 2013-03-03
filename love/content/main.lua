require 'lib.utils'
class  = require 'lib.30log'
local Entity = require 'class.entity'

-- Global var
global = {}
global.debug = true


function love.load()
end

function love.update(dt)
end

function love.draw()
end

function love.keypressed(key)
  if key == "escape" then
    love.event.push("quit")
  end
end
