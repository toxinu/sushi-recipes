function love.conf(t)
  t.screen.width = 600
  t.screen.height = 600
  t.screen.vsync = true
  t.title = "{{ app|title }}"
  t.modules.physics = false
  t.modules.joystick = false
end
