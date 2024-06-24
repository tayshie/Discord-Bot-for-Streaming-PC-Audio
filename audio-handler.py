import pyaudio
import wave
import asyncio
import discord

class AudioHandler:
    def __init__(self, config):
        self.chunk = config['audio']['chunk']
        self.format = getattr(pyaudio, config['audio']['format'])
        self.channels = config['audio']['channels']
        self.rate = config['audio']['rate']
        self.device_index = config['audio']['device_index']
        self.p = pyaudio.PyAudio()

    async def capture_audio(self, duration):
        stream = self.p.open(format=self.format,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             input_device_index=self.device_index,
                             frames_per_buffer=self.chunk)

        frames = []
        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = await asyncio.to_thread(stream.read, self.chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        return frames

    def save_audio(self, frames, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    async def stream_audio(self, voice_client, frames):
        if not voice_client.is_connected():
            return

        audio = discord.FFmpegPCMAudio(frames, pipe=True)
        voice_client.play(audio)

        while voice_client.is_playing():
            await asyncio.sleep(1)

    def cleanup(self):
        self.p.terminate()
