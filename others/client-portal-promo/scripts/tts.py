import json,asyncio,edge_tts
N=json.load(open('narration.json'))
async def main():
    for i,t in enumerate(N):
        await edge_tts.Communicate(t,'en-US-AriaNeural',rate='-4%').save(f'vo/{i}.mp3')
asyncio.run(main())
