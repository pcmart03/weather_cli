from setuptools import setup
setup(
    name="weather",
    version='0.1',
    py_modules=['weather', 'weather_request'],
    install_requires=["Click", "Requests", "texttable"],
    entry_points="""
        [console_scripts]
        weather=weather:cli
    """
)
