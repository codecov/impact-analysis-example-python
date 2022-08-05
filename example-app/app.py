from datetime import datetime
import os

from flask import (
    Flask,
    render_template,
)

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    BatchSpanProcessor,
    SimpleSpanProcessor,
)
from opentelemetry import trace

from codecovopentelem import (
    CoverageSpanFilter,
    get_codecov_opentelemetry_instances,
)
from utils.time import format_time

provider = TracerProvider()
trace.set_tracer_provider(provider)

current_version = os.getenv("CURRENT_VERSION", "0.0.2")
current_env = os.getenv("APP_ENV", "production")
export_rate = 100
untracked_export_rate = 0

generator, exporter = get_codecov_opentelemetry_instances(
    repository_token=os.getenv("CODECOV_OPENTELEMETRY_TOKEN"),
    version_identifier=current_version,
    sample_rate=export_rate,
    filters={
        CoverageSpanFilter.regex_name_filter: None,
        CoverageSpanFilter.span_kind_filter: [
            trace.SpanKind.SERVER,
            trace.SpanKind.CONSUMER,
        ],
    },
    code=f"{current_version}:{current_env}",
    untracked_export_rate=untracked_export_rate,
    environment=current_env,
)
provider.add_span_processor(generator)
provider.add_span_processor(BatchSpanProcessor(exporter))
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))


app = Flask(
    __name__,
    static_url_path='',
    static_folder='',
    template_folder='templates',
)
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/time')
def current_time():
    return render_template(
        'time.html',
        time=format_time(datetime.now()),
    )
