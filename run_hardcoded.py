from mbag.agents.elle_hardcoded_agents import *
from mbag.environment.goals.simple import BasicGoalGenerator
from mbag.evaluation.evaluator import MbagEvaluator
from malmo import minecraft
import os
import time

# Create output directory for video
out_dir = os.path.join(os.getcwd(), "hardcoded_video")
os.makedirs(out_dir, exist_ok=True)
print(f"Video will be saved to: {out_dir}")

# Launch MALMO first - we need 2 instances: 1 for agent, 1 for spectator
print("Launching MALMO...")
minecraft_process = minecraft.launch(num_instances=2)

# Create environment config
env_config = {
    "world_size": (5, 5, 5),
    "num_players": 1,
    "horizon": 50,
    "goal_generator": BasicGoalGenerator,
    "goal_generator_config": {},
    "malmo": {
        "use_malmo": True,        # Enable MALMO
        "use_spectator": True,    # Enable spectator for video
        "video_dir": out_dir,     # Where to save the video
        "action_delay": 0.8,      # Delay between actions
    },
    "abilities": {
        "teleportation": True,
        "flying": True,
        "inf_blocks": True,
    },
}

try:
    # Create evaluator with the hardcoded resource agent
    evaluator = MbagEvaluator(
        env_config,
        [(SimpleGoalGeneratorAgent, {})],  # Use the hardcoded agent
    )

    # Run the episode
    print("Starting episode...")
    episode_info = evaluator.rollout()
    print(f"Episode completed with reward: {episode_info.cumulative_reward}")
finally:
    # Clean up MALMO process
    print("Terminating MALMO...")
    # Give processes a moment to finish
    time.sleep(1)
    for process in minecraft_process:
        try:
            process.terminate()
            process.wait(timeout=2)  # Wait up to 2 seconds for process to terminate
        except:
            pass  # Ignore any errors during termination