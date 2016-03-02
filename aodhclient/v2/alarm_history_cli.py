#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from cliff import lister

from aodhclient import utils


class CliAlarmHistorySearch(lister.Lister):
    """Show history for all alarms based on query"""

    COLS = ('alarm_id', 'timestamp', 'type', 'detail')

    def get_parser(self, prog_name):
        parser = super(CliAlarmHistorySearch, self).get_parser(prog_name)
        parser.add_argument("--query", help="Query"),
        return parser

    def take_action(self, parsed_args):
        history = self.app.client.alarm_history.search(query=parsed_args.query)
        return utils.list2cols(self.COLS, history)


class CliAlarmHistoryShow(lister.Lister):
    """Show history for an alarm"""

    COLS = ('timestamp', 'type', 'detail')

    def get_parser(self, prog_name):
        parser = super(CliAlarmHistoryShow, self).get_parser(prog_name)
        parser.add_argument("alarm_id", help="ID of an alarm")
        return parser

    def take_action(self, parsed_args):
        history = self.app.client.alarm_history.get(
            alarm_id=parsed_args.alarm_id)
        return utils.list2cols(self.COLS, history)
