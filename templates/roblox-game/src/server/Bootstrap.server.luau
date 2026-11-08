--!strict
-- Minimal boot signal. This is NOT a complete game and confers no release readiness.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("GameShared"):WaitForChild("Config"))
print("[GameServer] " .. Config.GameName .. " preproduction bootstrap")
