Title: GPG key transition
Date: 2010-06-03 12:27
Author: Thierry Carrez
Tags: Announcements
Slug: gpg-key-transition

I've recently set up a stronger (4096R) OpenPGP key, and will be
transitioning away from my old (1024D) one. The old key will continue to
be valid for some time, but i prefer all future correspondence to come
to the new one. I would also like this new key to be re-integrated into
the web of trust. Please find here a [statement signed both
keys](http://people.ubuntu.com/~ttx/gpg_transition.txt), certifying the
transition.

The old key was:

    pub   1024D/B6A55F4F 2004-04-01
          Key fingerprint = 67FE 2899 7E9D 9D03 F1E7  C8BB BDC2 F5A1 B6A5 5F4F
     

And the new key is:

    pub   4096R/25B10423 2010-05-25
          Key fingerprint = 22A7 9430 50DB 1E67 EC2B  641A 507A F890 25B1 0423
     

To fetch my new key from a public key server, you can simply do:

      gpg --keyserver pgp.mit.edu --recv-key 25B10423
     

If you already know my old key, you can now verify that the new key is
signed by the old one:

      gpg --check-sigs 25B10423
     

If you don't already know my old key, or you just want to be double
extra paranoid, you can check the fingerprint against the one above:

      gpg --fingerprint 25B10423
     

If you are satisfied that you've got the right key, and the UIDs match
what you expect, I'd appreciate it if you would sign my key:

      gpg --sign-key 25B10423
     

Lastly, if you could upload these signatures, I would appreciate it. You
can either send me an e-mail with the new signatures or you can just
upload the signatures to a public keyserver directly:

      gpg --keyserver pgp.mit.edu --send-key 25B10423
     

Thanks !
