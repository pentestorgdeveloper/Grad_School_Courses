import mp1_certbuilder
from cryptography.hazmat.primitives.serialization import Encoding


def create_privKeys(p1, q1, p2, q2):
    privkey_1, pubkey1 = mp1_certbuilder.make_privkey(p1, q1)
    privkey_2, pubkey2 = mp1_certbuilder.make_privkey(q2, p2)
    netid = 'fisiaka2'
    cert1 = mp1_certbuilder.make_cert(netid, pubkey1)
    cert2 = mp1_certbuilder.make_cert(netid, pubkey2)
    print(cert1)
    print(cert2)
    with open('sol_1.2.5_certA.cer', 'wb') as f:
        f.write(cert1.public_bytes(Encoding.DER))
    with open('sol_1.2.5_certB.cer', 'wb') as f:
        f.write(cert2.public_bytes(Encoding.DER))
    with open('sol_1.2.5_factorsA.hex', 'wb') as f:
        f.write(str(hex(p1)) + '\n')
        f.write(str(hex(q1)))
    with open('sol_1.2.5_factorsB.hex', 'wb') as f:
        f.write(str(hex(p2)) + '\n')
        f.write(str(hex(q2)))
    return cert1, cert2

if __name__ == '__main__':
    p1 = 1917435062465656889557611846460125190576094634249653106821084547095299310209902577477454183002933306907248750681833261399926522380928590919704103962489
    p2 = 2368900048797717644092584464802057502397336097521617593766131409062879078742870097431862401491927107613946923625214101289228306347322812004390721568319
    q1 = 14078270178311247653357110009035776837144461295855036476582468749316118243911439434363680684258190842438454553911642858404298530652356250776817870679087389438788476176396782220748969151412601422637008714140354801061064464325156033384502083236491298245412039746913675328596536796273629310305076554142549451977536525862043833547465939909599895876487280798583242189794004985269151824504556212388975753316477246547397312921944220353539428111114347113703503040609881832387
    q2 = 11395233358393027054619626177473491300213608199449838002732141477293752775124482294864156439013885020280802870738230085263223975084564663985882693876171061665498216734207392036990192967045191791937043535671480715398964269829713007715698628388378498242062489350918768527973094881693436683897215580013478750813651293064169461687472136304430257290626640541545642239984730104363146051490997563587460311371742959289133837996813303343711863851353274761638952062259890784021
    print hex(p1*q1)
    print hex(p2*q2)
    print hex(p1*q2)
    print hex(p2*q1)

    create_privKeys(p1=p1,
                    q1=q1,
                    p2=p2,
                    q2=q2)

