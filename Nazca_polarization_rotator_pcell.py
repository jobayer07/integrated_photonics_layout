import nazca as nd
from nazca.interconnects import Interconnect
import nazca.pdk_template as pdk


#@nd.bb_util.hashme('polarization_rotator', 'label')
def polarization_rotator(bot_escalator_length=90, bot_escalator_out_width=0.8, top_escalator_length=79.5, top_escalator_in_width=0.125, top_escalator_out_width=1.86, escalator_stabilize_length=10, rotator_length=99.99, bot_rotator_out_width=0.75, bot_rotator_shift=1.275, top_rotator_out_width=1.42, rotator_stabilize_length=25.01, bot_horizontal_length=10, final_taper_length=15, top_away_length=15, top_away_final_width=0.125, waveguide_width=1.2, label=''):
    with nd.Cell(name='rotator') as pl:

        bot = Interconnect(xs='FNAM Waveguide')
        bot_in=bot.taper(length=bot_escalator_length, width1=waveguide_width, width2=bot_escalator_out_width, arrow=False).put()
        bot.taper(length=escalator_stabilize_length, width1=bot_escalator_out_width, width2=bot_escalator_out_width, arrow=False).put()
        bot.taper(length=rotator_length, width1=bot_escalator_out_width, width2=bot_rotator_out_width, arrow=False, shift=bot_rotator_shift).put()
        bot.taper(length=rotator_stabilize_length, width1=bot_rotator_out_width, width2=bot_rotator_out_width, arrow=False, shift=bot_rotator_shift/2).put()
        bot.taper(length=bot_horizontal_length, width1=bot_rotator_out_width, width2=bot_rotator_out_width, arrow=False).put()
        bot_out=bot.taper(length=final_taper_length, width1=bot_rotator_out_width, width2=waveguide_width, arrow=False).put()
        
        nd.Pin("opt1", pin=bot_in.pin['a0']).put()
        nd.Pin("opt2", pin=bot_out.pin['b0']).put()
        nd.put_stub(length=0)
        nd.netlist.Annotation(text=label, layer=(980,727)).put(0, 0)
        
        top = Interconnect(xs='SNAM Waveguide')
        t1=top.taper(length=top_escalator_length, width1=top_escalator_in_width, width2=top_escalator_out_width, arrow=False).put(bot_escalator_length-top_escalator_length-0.001, 0)
        top.taper(length=escalator_stabilize_length, width1=top_escalator_out_width, width2=top_escalator_out_width, arrow=False).put()
        top.taper(length=rotator_length, width1=top_escalator_out_width, width2=top_rotator_out_width, arrow=False).put()
        top.taper(length=rotator_stabilize_length, width1=top_rotator_out_width, width2=top_rotator_out_width, arrow=False).put()
        top.taper(length=top_away_length, width1=top_rotator_out_width, width2=top_away_final_width, arrow=False, shift=(-top_rotator_out_width+top_away_final_width)/2).put()
        
    return pl