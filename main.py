from flask import Flask
from threading import Thread
import nextcord
import jishaku
from flask import jsonify
from nextcord.ext import commands
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix = '?', intents=intents)
app = Flask('')
import os

@app.route('/')
def home():
    return "Hello. I am alive!"

@app.route('/spotify/<user_id>')
def spotify(user_id):
    member = bot.get_guild(935438603960590336).get_member(int(user_id))
    if member is None:
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "coding",
                "message": 'NOT FOUND',
                "color": "red"
            }
        )
    elif member.activity is not None:
        if isinstance(member.activity, nextcord.Spotify):
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "listening",
                    "message": member.activity.title,
                    "color": "green"
                }
            )

        else:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "listening",
                    "message": 'nothing rn',
                    "color": "green"
                }
            )
    else:
        return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "listening",
                    "message": 'nothing rn',
                    "color": "green"
                }
            )

@app.route('/vscode/<user_id>')
def vscode(user_id):
    member = bot.get_guild(935438603960590336).get_member(int(user_id))
    if member is None:
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "coding",
                "message": 'NOT FOUND',
                "color": "red"
            }
        )
    elif member.activity is not None:
        if member.activity.name.lower() == 'visual studio code':
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "coding",
                    "message": member.activity.details,
                    "color": "blue"
                }
            )

        else:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "coding",
                    "message": 'nothing rn',
                    "color": "blue"
                }
            )
    else:
        return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "coding",
                    "message": 'nothing rn',
                    "color": "blue"
                }
            )

@app.route('/status/<user_id>')
def status(user_id):
    member = bot.get_guild(935438603960590336).get_member(int(user_id))
    if member is None:
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "currently",
                "message": 'NOT FOUND',
                "color": "red"
            }
        )
    else:
        if member.status == nextcord.Status.dnd:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "currently",
                    "message": 'dnd',
                    "color": "red"
                }
            )
        elif member.status == nextcord.Status.online:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "currently",
                    "message": 'online',
                    "color": "green"
                }
            )
        elif member.status == nextcord.Status.offline:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "currently",
                    "message": 'offline',
                    "color": "inactive"
                }
            )
        elif member.status == nextcord.Status.idle:
            return jsonify(
                {
                    "schemaVersion": 1,
                    "label": "currently",
                    "message": 'idle',
                    "color": "yellow"
                }
            )

@app.route('/playing/<user_id>')
def playing(user_id):
    member = bot.get_guild(935438603960590336).get_member(int(user_id))
    if member is None:
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "playing",
                "message": 'NOT FOUND',
                "color": "red"
            }
        )
    elif member.activity is not None:
        if (not member.activity.name.lower() == 'visual studio code') and member.activity.type == nextcord.ActivityType.playing:
            return jsonify(
            {
                "schemaVersion": 1,
                "label": "playing",
                "message": member.activity.details,
                "color": "blueviolet"
            }
            )
        else:
            return jsonify(
            {
                "schemaVersion": 1,
                "label": "playing",
                "message": 'nothing rn',
                "color": "blueviolet"
            }
            )
    else:
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "playing",
                "message": 'nothing rn',
                "color": "blueviolet"
            }
            )
def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.command()
async def henlo(ctx):
    await ctx.send('hi')

bot.load_extension('jishaku')

keep_alive()
bot.run(os.environ['token'])
